# Spanish Hyphenation in pdfTeX with Babel v25.4: Technical Deep Dive

**The absence of "Hyphen rules for 'spanish' set to \l@spanish" log messages when using `\babelprovide[import,main]` is expected behavior, not a bug.** This modern loading method uses fundamentally different mechanisms than classical `\usepackage[spanish]{babel}`, resulting in reduced logging verbosity while still activating hyphenation patterns correctly. The key requirement is that Spanish patterns must be preloaded in the pdfTeX format file during format generation, and `\babelprovide[import,main]{spanish}` will then activate them automatically when used after English is loaded.

## Understanding `\babelprovide[import,main]` mechanics in pdfTeX

Babel v25.4, released February 14, 2025, provides two distinct methods for loading languages: the classical approach using language definition files (.ldf) and the modern approach using ini configuration files. The `\babelprovide[import,main]{spanish}` command represents the modern method and operates through a modular, data-driven architecture based on Unicode Common Locale Data Repository standards.

When `\babelprovide[import,main]{spanish}` executes in pdfTeX, it performs several critical operations. The **import option** loads full locale data from `babel-es.ini`, including captions (chapter names, figure labels), date formatting patterns, hyphenation minimums, and LICR (LaTeX Internal Character Representation) variants for pdfTeX. For 8-bit engines like pdfTeX, the command loads LICR macros rather than UTF-8 variants, converting accented characters into commands like `\'a` and `\~n`. The **main option** overrides any previously set main language, making Spanish the document's primary language that activates automatically at `\begin{document}`.

The expected behavior when Spanish is loaded after English differs significantly from simply loading Spanish initially. When you execute `\usepackage[english]{babel}` followed by `\babelprovide[import,main]{spanish}`, the sequence creates this state: English is loaded first and recognized globally, then Spanish becomes the new main language through the main parameter, overriding English's primary status. At document start, Spanish hyphenation patterns activate, Spanish captions replace English ones, and `\today` prints dates in Spanish format. Both languages remain available for switching via `\selectlanguage`, but Spanish now functions as the default.

With pdfTeX version 3.84 and later, languages loaded on-the-fly using `\babelprovide` automatically receive font encoding support based on `fontenc` configuration, but this only works for specific scripts: Latin, Cyrillic, Greek, Arabic, Hebrew, Cherokee, Armenian, and Georgian. This represents a significant enhancement over earlier versions, though pdfTeX still cannot load hyphenation patterns dynamically during document processing like LuaTeX can.

## The critical distinction between .tex patterns and format compilation

A fundamental source of confusion involves the relationship between hyphenation pattern files and what pdfTeX actually uses. **There is no standard .hyp compiled format in TeX Live**—this terminology does not appear in official pdfTeX documentation. Instead, the system works through a two-stage process that compiles plain text patterns into binary format files.

Hyphenation patterns exist as plain text `.tex` files, such as `hyph-es.tex` located in `/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/tex/`. These files contain `\patterns{...}` and `\hyphenation{...}` commands with sequences like `.ach4` and `e1n2a`, where numbers indicate hyphenation levels (odd numbers allow breaks, even numbers forbid them) and dots represent word boundaries. During format creation via `pdftex -ini`, the system reads configuration files (`language.dat` or `language.def`), loads the specified pattern files for enabled languages, assigns each language a `\language` number, and compiles everything into `.fmt` binary files containing preloaded patterns, font metrics, and LaTeX commands.

The mere presence of `hyph-es.tex` in the patterns directory **does not guarantee** Spanish hyphenation will work. Four requirements must be met: the pattern file must exist, the language must be enabled in `language.def` configuration, the format file must be regenerated after configuration changes using `fmtutil --all` or `fmtutil --byfmt pdflatex`, and babel must be loaded in the document with the Spanish option. The common warning "No hyphenation patterns were preloaded for the language 'Spanish' into the format" indicates patterns were not loaded during format generation, even if the source `.tex` file exists.

For modern eTeX-based formats like pdfLaTeX, the `language.def` file controls pattern loading rather than the older `language.dat`. This file contains `\addlanguage` commands with additional parameters specifying left and right hyphenation minimums. The `babel-es.ini` file serves a different purpose entirely—babel reads this at document processing time (not format generation time) to obtain language metadata, captions, and configuration, but the hyphenation patterns themselves come from the precompiled format.

## Why log messages differ between loading methods

The logging behavior differences between `\usepackage[spanish]{babel}` and `\babelprovide[import,main]{spanish}` stem from fundamentally different loading mechanisms, not bugs or incomplete implementation. Classical loading through package options executes the Spanish .ldf file directly, performs explicit hyphenation pattern allocation with verbose logging, fully initializes all language features including captions, dates, and shorthands, and generates messages like "Package babel Info: Hyphen rules for 'spanish' set to \l@spanish" showing the explicit allocation.

The modern `\babelprovide` approach operates differently. It primarily focuses on configuration and auxiliary tasks, may silently reuse existing patterns already loaded in the format, performs minimal language setup unless the import option is specified, and uses less verbose logging by default. GitHub issue #124 in the babel repository reveals that when hyphenrules are successfully mapped to existing patterns, babel may generate alternative info messages like "Package babel Info: \l@<language> = using hyphenrules for <other>" rather than the standard allocation message. The absence of the traditional "set to \l@spanish" message does not indicate failure—it simply reflects that `\babelprovide` is reusing patterns already present in the format rather than allocating them from scratch.

When Spanish hyphenation patterns are successfully loaded via `\babelprovide[import,main]`, you should look for different indicators in the log file. If patterns are preloaded in the format, babel activates them silently and you won't see allocation warnings. If patterns are **not** preloaded, you'll see the explicit warning: "Package babel Warning: No hyphenation patterns were preloaded for the language 'Spanish' into the format... Now I will use the patterns preloaded for \language=0 instead." This warning clearly indicates hyphenation failure. Additionally, info messages about loading data from ini files appear, including standardized language and script names, BCP 47 tags, and script information.

## Technical verification methods for confirming active hyphenation

Verifying that Spanish hyphenation patterns are actually active requires using specific pdfTeX primitives and babel commands. The most fundamental tool is the **`\the\language`** command, which displays the numeric ID of the currently active hyphenation pattern set. When you compile a document containing `\the\language`, if it shows 0, this typically indicates no hyphenation or English fallback patterns. Any other number (3, 5, 15, etc.) indicates a specific language is active, though the exact number varies by installation.

The **`\showhyphens{}`** command represents the most powerful debugging tool for hyphenation verification. When you write `\showhyphens{administración México palabras}` in your document, pdfTeX outputs all possible hyphenation points to the terminal and log file (not the PDF). A typical log entry appears as `[] \OT1/cmr/m/n/10 ad-min-is-tra-ción Méx-i-co pal-abras`, showing every permitted break point according to the currently active patterns. This provides definitive proof that patterns are working correctly.

For checking which language number corresponds to Spanish, you can use the `showlanguages` package option. Loading babel with `\usepackage[spanish,showlanguages]{babel}` causes the log file to display a complete mapping like "language 0: nohyphenation dumylang (no exceptions), language 1: english (no exceptions), language 3: spanish eshyph.tex (no exceptions)." This reveals the exact numeric assignment for your installation.

The **`\languagename`** macro (or better, **`\localename`** in babel 24.10+) returns the current language name as a string such as "spanish" or "english". While useful for display, the documentation cautions against using `\languagename` for conditionals and recommends `\localename` instead. Additional primitives provide fine-grained information: `\the\lefthyphenmin` and `\the\righthyphenmin` show minimum characters required before and after hyphens, while `\the\hyphenchar\font` displays the current hyphen character code (usually 45 for the standard hyphen).

A complete verification workflow combines these tools systematically. Create a test document that checks the language name with `\languagename`, displays the language number with `\the\language`, tests hyphenation points by examining the log file after `\showhyphens{administración universidad México}`, forces visible hyphenation with `\parbox{1cm}{administración}`, and verifies hyphenation parameters with `\the\lefthyphenmin` and `\the\righthyphenmin`. If your PDF shows "spanish" with a number greater than 0, the log contains hyphenation points like "ad-min-is-tra-ción", the narrow parbox displays actual hyphens, and no "No hyphenation patterns" warning appears, then Spanish hyphenation is functioning correctly.

## Language precedence and the role of the main parameter

When English loads first through a document class option and Spanish is subsequently loaded via `\babelprovide[import,main]`, the main parameter **does guarantee** Spanish becomes the primary hyphenation language, with important caveats. According to babel v25.4 documentation, the main option "makes the language the main one (thus overriding that set when babel is loaded)," which means Spanish hyphenation patterns activate at document start, Spanish captions become default, Spanish date format applies to `\today`, `\localename` returns "spanish", and Spanish becomes the return language after `\foreignlanguage` calls end.

The sequence `\documentclass[english]{article}` followed by `\usepackage{babel}` and then `\babelprovide[import,main]{spanish}` creates this final state: the class option makes English globally known, babel loads with English support initially, but the import option loads full Spanish locale data from the ini file, and the main option overrides English as the primary language. At `\begin{document}`, Spanish is active rather than English.

This differs significantly from omitting the main parameter. When you use `\babelprovide[import]{spanish}` without main, Spanish loads but does **not** become primary—English remains the default and you must explicitly call `\selectlanguage{spanish}` to switch. The main parameter provides automatic activation without requiring explicit selection commands.

However, proper hyphenation requires more than just the main parameter. Patterns must be preloaded in the format file during format generation, proper font encoding must be configured using `\usepackage[T1]{fontenc}` since the default OT1 encoding doesn't support accented characters properly, and UTF-8 input encoding should be used (though this is default since LaTeX 2018). If these prerequisites aren't met, you'll see the format warning even with correctly used main parameter.

## Commands for activating and controlling hyphenation

The critical distinction that causes significant confusion is that **hyphenation activation and language shorthands are completely separate systems**. The commands `\useshorthands{"}` and `\languageshorthands{spanish}` activate typing shortcuts—not hyphenation patterns. Spanish shorthands include `"<` and `">` for quotation marks (« »), `"-` for explicit hyphenation points, and `"~` for non-breaking hyphens. You can enable Spanish shorthands in English text without changing hyphenation patterns at all.

Spanish hyphenation patterns activate automatically through three mechanisms. Loading Spanish as a package option with `\usepackage[spanish]{babel}` activates patterns at the document level. Using `\selectlanguage{spanish}` switches to Spanish patterns for all subsequent text, performing comprehensive language switching including hyphenation, captions, dates, shorthands, and locale settings. For localized hyphenation in short phrases, `\foreignlanguage{spanish}{texto}` applies Spanish patterns only to the enclosed text without changing document-wide settings.

The `\babelhyphenmins{spanish}{2}{2}` command provides fine control over hyphenation behavior by setting minimum character counts before and after hyphen points, but **it is not sufficient alone** to activate hyphenation. This command merely adjusts parameters for already-loaded patterns. Complete hyphenation requires that patterns be preloaded in the format, the language be selected via babel loading or `\selectlanguage`, and appropriate font encoding be configured with T1 fontenc.

For adding custom hyphenation exceptions beyond the loaded patterns, use `\babelhyphenation[spanish]{mate-máti-cas recu-perar}` in the preamble. This defines specific break points for words that patterns might not handle correctly. The babel v25.4 documentation notes that Spanish patterns in standard TeX distributions typically have sensible defaults, so explicitly setting `\babelhyphenmins` is usually unnecessary unless you need fine-tuning for specific typographic requirements.

The modern correct way to activate hyphenation in babel v25.4 when loading languages dynamically with `\babelprovide` is to use `\babelprovide[import,main]{spanish}` which combines importing locale data with making Spanish the main language, or use `\babelprovide[import]{spanish}` followed by explicit `\selectlanguage{spanish}` calls when needed. The classical method `\usepackage[spanish]{babel}` remains the recommended approach for pdfTeX when the language definition file exists and works properly.

## How `\selectlanguage{spanish}` affects hyphenation comprehensively

The `\selectlanguage{spanish}` command performs far more than simply switching hyphenation patterns—it executes comprehensive language switching across multiple subsystems. When called, it activates Spanish hyphenation patterns by setting the `\language` primitive register to Spanish's assigned number, switches captions so commands like `\chaptername` and `\figurename` produce Spanish text, changes date formatting so `\today` prints Spanish format, activates language-specific extras by running `\extrasspanish` (including shorthands and spacing rules), writes language information to auxiliary files affecting headers, footers, and table of contents, and sets the locale so `\localename` returns "spanish".

The hyphenation-specific effects are immediate and persistent. Before executing `\selectlanguage{spanish}`, all text uses the previously active language's patterns. After execution, all subsequent text uses Spanish patterns until another `\selectlanguage` call changes the active language. This differs from `\foreignlanguage{spanish}{text}` which applies Spanish hyphenation only to the enclosed text without changing global caption or date settings.

Babel v25.4 documentation provides important warnings about `\selectlanguage` usage. In vertical mode, the command inserts a `\write` operation that can break vertical spacing in some contexts. Using `\selectlanguage` inside braces may have non-local effects persisting beyond the group. The language can become out of sync with `\bibitem` and floats since auxiliary file writing occurs at page shipout rather than at the point of execution. For short phrases where only hyphenation matters without changing captions or dates, prefer `\foreignlanguage{spanish}{texto}` which avoids these complications.

## Recommended configurations and practical solutions

For the common scenario where a document class loads English but Spanish support with correct hyphenation is needed, several configuration approaches exist with different trade-offs. The **best practice for pdfTeX** is the classical method that remains most reliable: `\usepackage[english,spanish]{babel}` where the last language in the option list becomes main. Spanish activates at document start while English remains available via `\selectlanguage{english}`. This approach provides tested stability, full feature support, and maximum compatibility.

When you cannot modify class options or they force English, use **option passing** before the document class: `\PassOptionsToPackage{main=spanish,english}{babel}` followed by `\documentclass[english]{article}` and `\usepackage{babel}`. This explicitly makes Spanish the main language regardless of class options, ensuring proper precedence. The `\PassOptionsToPackage` must appear before `\documentclass` to affect babel loading.

For users wanting modern ini-based features, the recommended pattern is `\usepackage{babel}` (without language options) followed by `\babelprovide[import,main]{spanish}` and `\babelprovide[import]{english}` in the preamble. This loads Spanish as main using ini files while keeping English available as secondary. However, this approach is best reserved for cases where language definition files don't exist or need customization, since the classical method remains more thoroughly tested for languages with existing .ldf files.

The complete working configuration addressing all potential issues combines proper font encoding, correct babel loading, and verification commands:

```latex
\documentclass[english]{article}
\usepackage[T1]{fontenc}  % Critical for Spanish accents in pdfTeX
\PassOptionsToPackage{main=spanish,english}{babel}
\usepackage{babel}

\begin{document}
% Verify Spanish is active:
% Current language: \languagename (should show: spanish)
% Language number: \the\language (should show: non-zero)

Texto español con acentuación correcta y separación silábica.

\selectlanguage{english}
English text with proper hyphenation.

\foreignlanguage{spanish}{Breve texto español sin cambiar idioma global.}
\end{document}
```

## Troubleshooting missing patterns and verification

The most common issue is the "No hyphenation patterns were preloaded" warning appearing despite having pattern files installed. This indicates the format file lacks Spanish patterns even though source files exist. **The solution requires format regeneration**, not package reinstallation. First verify pattern availability with `kpsewhich hyph-es.tex` which should return the full path. Then check whether Spanish is enabled in the configuration by examining `language.def` for an entry like `\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}`. If missing, enable Spanish in your TeX distribution's language configuration interface (varies by distribution).

After enabling Spanish in configuration, **rebuild format files** using the command appropriate for your system: for TeX Live use `fmtutil-sys --all` to rebuild all formats or `fmtutil-sys --byfmt pdflatex` for just pdfLaTeX, while MiKTeX users should open Settings, navigate to Formats, and click Build. This regeneration compiles pattern files into the binary format file that pdfTeX uses. Check the format date in your log file header after regeneration—it should reflect the rebuild date.

For cases where hyphenation appears not to work despite successful pattern loading, verify font encoding first. The default OT1 encoding cannot properly handle accented characters, breaking hyphenation for words containing accents. Always use `\usepackage[T1]{fontenc}` with Spanish. Second, confirm pattern preload by examining the log for warnings. Third, ensure explicit language selection with `\selectlanguage{spanish}` when using `\babelprovide` without the main parameter. Fourth, try adjusting hyphenation minimums with `\babelhyphenmins{spanish}{2}{2}` if patterns are active but hyphenation seems too conservative.

The fastest verification approach uses `\showhyphens{administración universidad internacionalización}` and examines the log file output. If you see `ad-min-is-tra-ción`, `uni-ver-si-dad`, and proper break points, patterns are working correctly. If no hyphens appear or all words remain unbroken in the log output, patterns are not active despite what other indicators might suggest.

## Key distinctions and technical conclusions

Several critical technical points emerge from this analysis that clarify common confusion. The `\babelprovide` mechanism loads language metadata and activates existing patterns but cannot load patterns dynamically in pdfTeX—patterns must be precompiled into format files during format generation using `fmtutil`. Different log messages appear with `\babelprovide` versus classical loading because `\babelprovide` silently reuses existing patterns rather than allocating them explicitly, making the absence of allocation messages expected behavior rather than a sign of failure.

Shorthands and hyphenation represent completely separate systems: `\useshorthands` and `\languageshortands` affect typing shortcuts while having zero effect on hyphenation, which is controlled exclusively by pattern loading and language selection commands. The main parameter in `\babelprovide[import,main]{spanish}` does guarantee Spanish becomes the primary hyphenation language, but only if patterns exist in the format—the main parameter activates existing patterns but cannot create them if they weren't preloaded.

For pdfTeX users, the classical loading method `\usepackage[spanish]{babel}` remains the recommended approach when language definition files exist, providing tested stability and full feature support. Modern `\babelprovide` serves best for languages without .ldf files, customizing existing languages, or creating variants. The T1 font encoding is essential for proper Spanish hyphenation in pdfTeX, as the default OT1 encoding cannot correctly handle accented characters that Spanish requires.

The technical verification workflow must check multiple indicators simultaneously: `\the\language` should show non-zero, `\languagename` should display "spanish", `\showhyphens{}` output in the log should show proper break points, no "No hyphenation patterns were preloaded" warning should appear, and actual narrow text columns should display visible hyphens when forcing line breaks. Only when all these indicators confirm proper operation can you trust that Spanish hyphenation is fully functional.

Understanding these distinctions resolves the apparent mystery of missing log messages—they're not missing, they simply indicate a different loading mechanism that achieves the same functional result through alternative means. When patterns are preloaded and `\babelprovide[import,main]{spanish}` executes, Spanish hyphenation activates correctly even without the traditional allocation message, provided the format contains the patterns and appropriate font encoding is configured.
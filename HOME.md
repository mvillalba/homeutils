$HOME Layout
============

Introduction
------------
Each section below describes a portion of my $HOME tree.

 * All text files are encoded in UTF-8 unless otherwise specified.
 * All directories of $HOME are revision-controlled individually (git+msync),
   synchronized (msync), and backed up automatically (msync) unless otherwise
   specified.


Deprecated
----------

 * ~/chl: Old ORGv1 challenges (largely in disuse).
 * ~/rfr: Reference data (nice in concept but never actually used it).
 * All plain-text notes are upper-case named, with no spaces, and no extension.


Notes
-----

 * ~/nts: Various quick note files on various things without much structure as
   well as some highly-structured note files moved here for easier access.
 * ~/nts/inbox: Notes too large/unstructured for standard inboxes that need be
   treated as normal inbox notes (ORGv1 wise). Files in this directory have a
   a dead simple format: PROJECTSPEC\n\=====\nCONTENT.
 * ~/nts/org: Current ORGv1 control files.
 * ~/nts/org/{U,N}-INBOX: ORGv1 urgent and normal inboxes, respectively.
 * ~/nts/NAME/NOTE: Free-form note files.


Journal
-------

 * ~/jrn: My personal journal.
 * ~/jrn/YYYY/MM/DD: Journal entry for YYYY-MM-DD, in Markdown-ish format.

Journal entries are formatted as follows:
"
YYYY-MM-DD [ISO-2LETTER-LANG] DAY-OF-WEEK
=========================================

GENERAL-SECTION-CONTENTS


SECTION-NAME
------------
SECTION-NAME-CONTENTS
"
When ISO-2LETTER-LANG is not specified, it will be infered from DAY-OF-WEEK.
DAY-OF-WEEK must be correct for YYYY-MM-DD. The GENERAL section is the default
section of the entry.

Any file in other parts of $HOME may refer to a journal entry with the
following spec: "jrn:YYYY-MM-DD/SECTION". The section spec must have no spaces,
must be upper-cased, and can be an unambiguous shortname for a larger section
(i.e. "HEALTH" for "Health & Fitness").


Projects
--------

 * ~/prj: Administrative project tree.
 * ~/prj/mgp: Mega-project codenamed MGP. Codenames must be 3-letter
   contractions of project named with no vowels.
 * ~/prj/mgp/nmp: Normal-project codenamed MGP-NMP. Naming rules are the same
   as those used for mega-projects.
 * ~/prj/mgp/nmd/subproject: Sub-project codenamed MGP-NMP/SubProject.
   Free-form contractions with vowels and no length restrictions are allowed
   for sub-projects (they are second-class citizens), but keep it reasonable
   and do not use whitespaces.


System
------

 * ~/sys: Local utilities and control repositories.
 * ~/sys/local: Where locally-installed programs get installed. Not
   revision-controlled.
 * ~/sys/local/NAME: Individual program install root tree.
 * ~/sys/dotfiles: My dotfiles.
 * ~/sys/scripts: Assorted useful scripts added to my $PATH.
 * ~/sys/gitolite: Gitolite config for my server.
 * ~/sys/tmp: A local temp directory for programs to use. Not
   revision-controlled.
 * ~/sys/NAME: Generic repository with important control data (puppet confs,
   FAI confs, etc).


Vault
-----

 * ~/vlt: Large, mostly binary data collections of all sorts.
 * ~/vlt/download: Non revision-controlled download directory for Web browsers.
   Automatically purged of old files (30+ days == old).
 * ~/vlt/system: Non revision-controlled system-images directory. Mainly
   useful ISOs.
 * ~/vlt/podcast: Non revision-controlled podcast download directory for music
   players.
 * ~/vlt/photo: Photo archive.
 * ~/vlt/photo/COL/SUB-COL/SUB-SUB-COL/photo.jpg: Photography in a 3-level,
   nested collection.
 * ~/vlt/backup: Where backups go to die. Not revision-controlled.
 * ~/vlt/backup/msync: Local mirror of active backup repository.
 * ~/vlt/backup/NAME: Manual backups for other things (usually saving stuff
   for friends).
 * ~/vlt/music: My music. All legal, I promiss.
 * ~/vlt/music/modern: Non-classical music.
 * ~/vlt/music/classic: Classical music.
 * ~/vlt/NAME: Generic, opaque data repository.


Workspaces
----------

 * ~/wks: Free-form workspaces for coding (or any other) projects, prototypes,
   experiments, tests, etc.
 * ~/wks/NAME: Specific workspace for destined for a particular purpose (i.e.
   "scius", "ant", "tungsteno", etc).

Workspaces are meant to be disposable and purged periodically (during ORGv1
reviews). Workspaces are not revision-controlled, nor synchronized anywhere.

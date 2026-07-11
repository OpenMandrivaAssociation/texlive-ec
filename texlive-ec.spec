%global tl_name ec
%global tl_revision 25033

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Computer modern fonts in T1 and TS1 encodings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ec
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ec.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The EC fonts are European Computer Modern Fonts, supporting the complete
LaTeX T1 encoding defined at the 1990 TUG conference hold at
Cork/Ireland. These fonts are intended to be stable with no changes
being made to the tfm files. The set also contains a Text Companion
Symbol font, called tc, featuring many useful characters needed in text
typesetting, for example oldstyle digits, currency symbols (including
the newly created Euro symbol), the permille sign, copyright, trade mark
and servicemark as well as a copyleft sign, and many others. Recent
releases of LaTeX2e support the EC fonts. The EC fonts supersede the
preliminary version released as the DC fonts. The fonts are available in
(traced) Adobe Type 1 format, as part of the cm-super bundle. The other
Computer Modern-style T1-encoded Type 1 set, Latin Modern, is not
actually a direct development of the EC set, and differs from the EC in
a number of particulars.


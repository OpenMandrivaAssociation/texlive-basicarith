%global tl_name basicarith
%global tl_revision 35460

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Macros for typesetting basic arithmetic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/basicarith
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for typesetting basic arithmetic, in the
style typically found in textbooks. It focuses on the American style of
performing these algorithms. It is written mostly in low-level TeX, with
the goal that it should run in either plain TeX or LaTeX, but there are
two constructions that currently prevent this. It is highly
configurable, with macros and lengths described in the documentation.


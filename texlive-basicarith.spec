Name:		texlive-basicarith
Version:	35460
Release:	2
Summary:	Macros for typesetting basic arithmetic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/basicarith
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basicarith.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting basic arithmetic,
in the style typically found in textbooks. It focuses on the
American style of performing these algorithms. It is written
mostly in low-level TeX, with the goal that it should run in
either plain TeX or LaTeX, but there are two constructions that
currently prevent this. It is highly configurable, with macros
and lengths described in the documentation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/basicarith
%{_texmfdistdir}/tex/latex/basicarith
%doc %{_texmfdistdir}/doc/latex/basicarith

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

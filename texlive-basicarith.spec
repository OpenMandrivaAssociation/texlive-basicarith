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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for typesetting basic arithmetic, in the
style typically found in textbooks. It focuses on the American style of
performing these algorithms. It is written mostly in low-level TeX, with
the goal that it should run in either plain TeX or LaTeX, but there are
two constructions that currently prevent this. It is highly
configurable, with macros and lengths described in the documentation.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/basicarith
%dir %{_datadir}/texmf-dist/source/latex/basicarith
%dir %{_datadir}/texmf-dist/tex/latex/basicarith
%doc %{_datadir}/texmf-dist/doc/latex/basicarith/CHANGES
%doc %{_datadir}/texmf-dist/doc/latex/basicarith/README
%doc %{_datadir}/texmf-dist/doc/latex/basicarith/basicarith.pdf
%doc %{_datadir}/texmf-dist/doc/latex/basicarith/lppl.txt
%doc %{_datadir}/texmf-dist/source/latex/basicarith/basicarith.dtx
%doc %{_datadir}/texmf-dist/source/latex/basicarith/basicarith.ins
%{_datadir}/texmf-dist/tex/latex/basicarith/basicarith.sty

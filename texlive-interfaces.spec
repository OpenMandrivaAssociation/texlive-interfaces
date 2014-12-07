# revision 21474
# category Package
# catalog-ctan /macros/latex/contrib/interfaces
# catalog-date 2011-02-19 16:41:47 +0100
# catalog-license lppl1.3
# catalog-version 3.1
Name:		texlive-interfaces
Version:	3.1
Release:	9
Summary:	Set parameters for other packages, conveniently
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/interfaces
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a small number of convenient macros that
access features in other frequently-used packages, or provide
interfaces to other useful facilities such as the pdfTeX
\pdfelapsedtime primitive. Most of these macros use pgfkeys to
provide a key-value syntax. The package also uses the package
scrlfile from the Koma-Script bundle (for controlled loading of
other files) and etoolbox. The package is bundled with sub-
packages containing actual interfaces: by default, the package
loads all available sub-packages, but techniques are provided
for the user to select no more than the interfaces needed for a
job.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/interfaces/interfaces-LaTeX.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-appendix.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-base.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-bookmark.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-embedfile.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-enumitem.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-environ.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-etoolbox.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-fancyhdr.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-hypbmsec.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-hyperref.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-makecell.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-marks.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-pgfkeys.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-scrlfile.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-tikz.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-titlesec.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-tocloft.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-truncate.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-umrand.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces.sty
%doc %{_texmfdistdir}/doc/latex/interfaces/README
%doc %{_texmfdistdir}/doc/latex/interfaces/interfaces.pdf
#- source
%doc %{_texmfdistdir}/source/latex/interfaces/interfaces.drv
%doc %{_texmfdistdir}/source/latex/interfaces/interfaces.dtx
%doc %{_texmfdistdir}/source/latex/interfaces/interfaces.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1-2
+ Revision: 752799
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1-1
+ Revision: 718725
- texlive-interfaces
- texlive-interfaces
- texlive-interfaces
- texlive-interfaces


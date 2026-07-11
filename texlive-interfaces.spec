%global tl_name interfaces
%global tl_revision 21474

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Set parameters for other packages, conveniently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/interfaces
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interfaces.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a small number of convenient macros that access
features in other frequently-used packages, or provide interfaces to
other useful facilities such as the pdfTeX \pdfelapsedtime primitive.
Most of these macros use pgfkeys to provide a key-value syntax. The
package also uses the package scrlfile from the Koma-Script bundle (for
controlled loading of other files) and etoolbox. The package is bundled
with sub-packages containing actual interfaces: by default, the package
loads all available sub-packages, but techniques are provided for the
user to select no more than the interfaces needed for a job.


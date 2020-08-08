%global common_desc							\
Nordic is a GTK3 theme created using the awseome Nord color pallete.


Name:		nordic-theme
Version:	1.9.0
Release:	1%{?dist}
Summary:	Flat theme using Nord color pallete

License:	GPLv3+
URL:		https://github.com/EliverLara/Nordic
Source0:	%{url}/releases/download/v%{version}/Nordic.tar.xz

BuildArch:	noarch

Requires:	gnome-themes-standard
Requires:	gtk-murrine-engine

%description
%{common_desc}


%prep
%setup -n Nordic

%install
mkdir -p %{buildroot}/usr/share/themes/
# install -m 777 -d %{_builddir}/Nordic %{buildroot}/usr/share/themes/Nordic
cp -a -r %{_builddir}/Nordic %{buildroot}/usr/share/themes/

# Need to run 
# gsettings set org.gnome.desktop.interface gtk-theme "Nordic"
# gsettings set org.gnome.desktop.wm.preferences theme "Nordic"
# gsettings set org.gnome.shell.extensions.user-theme name "Nordic"

%files
/usr/share/themes/Nordic

%changelog
* Fri Aug 7 2020 Tony Sweets <tony.sweets@gmail.com> - 1.9.0-1
- Initial Packaging

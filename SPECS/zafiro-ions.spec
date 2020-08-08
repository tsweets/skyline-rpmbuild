%global common_desc							\
Minimalist icons created with the flat-design technique, utilizing washed out colors and always accompanied by white. The priority is simplicity.


Name:		zafiro-icons
Version:	1.1
Release:	1%{?dist}
Summary:	Minimalist icons created with the flat-design technique

License:	GPLv3+
            
URL:        https://github.com/zayronxio/Zafiro-icons
Source0:	%{url}/archive/%{version}.zip

BuildArch:	noarch

Requires:	gnome-themes-standard
Requires:	gtk-murrine-engine

%description
%{common_desc}


%prep
%setup -n Zafiro-icons-1.1

%install
mkdir -p %{buildroot}/usr/share/icons/Zafiro
cp -a -r %{_builddir}/Zafiro-icons-1.1/* %{buildroot}/usr/share/icons/Zafiro

# Need to run 
# gsettings set org.gnome.desktop.interface gtk-theme "Nordic"
# gsettings set org.gnome.desktop.wm.preferences theme "Nordic"
# gsettings set org.gnome.shell.extensions.user-theme name "Nordic"

%files
/usr/share/icons/Zafiro

%changelog
* Fri Aug 7 2020 Tony Sweets <tony.sweets@gmail.com> - 1.1-1
- Initial Packaging

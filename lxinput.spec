# TODO
# - gtk3 possible:   --enable-gtk3           enable to use gtk-3.0 instead of gtk-2.0
Summary:	Keyboard and mouse configurator for LXDE
Name:		lxinput
Version:	0.3.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	948ad3371325f53bf8c4a7ed555558a4
URL:		http://www.lxde.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.40
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXInput is a small program used to configure keyboard and mouse for
LXDE.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxinput
%{_desktopdir}/lxinput.desktop
%{_datadir}/lxinput
%{_mandir}/man1/lxinput*

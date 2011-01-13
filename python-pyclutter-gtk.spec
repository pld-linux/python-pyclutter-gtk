Summary:	Python bindings for the clutter-gtk integration library
Summary(pl.UTF-8):	Dowiązania Pythona do biblioteki integrującej clutter-gtk
Name:		python-pyclutter-gtk
Version:	0.10.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://source.clutter-project.org/sources/pyclutter-gtk/0.10/pyclutter-gtk-%{version}.tar.bz2
# Source0-md5:	01ab4dc60e7d00737e372f38fdefa9f2
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.10.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pyclutter-devel >= 1.0.0
BuildRequires:	python-pygtk-devel >= 2:2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	clutter >= 1.0.0
Requires:	clutter-gtk >= 0.10.2
Requires:	python-pyclutter >= 1.0.0
Requires:	python-pygtk-gtk >= 2:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the clutter-gtk integration library.

%description -l pl.UTF-8
Dowiązania Pythona do biblioteki integrującej clutter-gtk.

%package devel
Summary:	Development files for Cutter-GStremer Python binding
Summary(pl.UTF-8):	Pliki programistyczne wiązania Pythona do Clutter-GStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.0.0
Requires:	clutter-gtk-devel >= 0.10.2
Requires:	python-pyclutter-devel >= 1.0.0
Requires:	python-pygtk-devel >= 2:2.8.0

%description devel
Development files for Cutter-GStremer Python binding.

%description devel -l pl.UTF-8
Pliki programistyczne wiązania Pythona do Clutter-GStreamer.

%prep
%setup -q -n pyclutter-gtk-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/cluttergtk/*.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{py_sitedir}/cluttergtk
%attr(755,root,root) %{py_sitedir}/cluttergtk/_cluttergtk.so
%{py_sitedir}/cluttergtk/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_datadir}/pyclutter/1.0/defs/cluttergtk*.defs
%{_pkgconfigdir}/pyclutter-gtk-0.10.pc

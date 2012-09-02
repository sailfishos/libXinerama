# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.24
# 

Name:       libXinerama

# >> macros
# << macros

Summary:    X.Org X11 libXinerama runtime library
Version:    1.1.2
Release:    1
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXinerama.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig

%description
API for Xinerama extension to X11 Protocol

%package devel
Summary:    X.Org X11 libXinerama development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
X.Org X11 Xinerama extension development package


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%doc README ChangeLog
%doc %{_mandir}/man3/*.3*
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h
# << files devel

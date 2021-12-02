%global commit0 d6b28414a4ceb41a904077318b48fa8a7d8981d1
%global date 20211202
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:       libevdi
Version:    1.9.1
Release:    3%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:    DisplayLink VGA/HDMI driver library
License:    LGPLv2+
URL:        https://github.com/DisplayLink/evdi

%if 0%{?tag:1}
Source0:    https://github.com/DisplayLink/evdi/archive/v%{version}.tar.gz#/evdi-%{version}.tar.gz
%else
Source0:    https://github.com/DisplayLink/evdi/archive/%{commit0}.tar.gz#/evdi-%{shortcommit0}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  libdrm-devel
BuildRequires:  make

%description
This adds support for HDMI/VGA adapters built upon the DisplayLink DL-6xxx,
DL-5xxx, DL-41xx and DL-3xxx series of chipsets. This includes numerous docking
stations, USB monitors, and USB adapters.

%prep
%if 0%{?tag:1}
%autosetup -p1 -n evdi-%{version}
%else
%autosetup -p1 -n evdi-%{commit0}
%endif

%build
cd library
%{set_build_flags}
%make_build

%install
cd library
%make_install LIBDIR=%{_libdir}

%files
%doc README.md
%license library/LICENSE
# DisplayLinkManager dlopens unversioned shared object:
%{_libdir}/libevdi.so
%{_libdir}/libevdi.so.0
%{_libdir}/libevdi.so.%{version}

%changelog
* Thu Dec 02 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-3.20211202gitd6b2841
- Update to latest snapshot.

* Thu Sep 02 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-2
- Move unversioned library to main package.
- Drop devel subpackage.

* Tue Apr 13 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-1
- First build.

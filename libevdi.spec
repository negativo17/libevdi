%global commit0 b884877267f11edaeb2a0f05201943e4252e22f2
%global date 20220725
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:       libevdi
Version:    1.12.0
Release:    1%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Summary:    DisplayLink VGA/HDMI driver library
License:    LGPLv2+
URL:        https://github.com/DisplayLink/evdi

%if 0%{?tag:1}
Source0:    %{url}/archive/v%{version}.tar.gz#/evdi-%{version}.tar.gz
%else
Source0:    %{url}/archive/%{commit0}.tar.gz#/evdi-%{shortcommit0}.tar.gz
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
* Tue Aug 09 2022 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1.20220725gitb884877
- Update to latest 1.12.0 snapshot.

* Sat Apr 30 2022 Simone Caronni <negativo17@gmail.com> - 1.11.0-1.20220428git39da217
- Update to 1.11.0 snapshot.

* Thu Mar 03 2022 Simone Caronni <negativo17@gmail.com> - 1.10.1-1
- Update to 1.10.1.

* Fri Jan 21 2022 Simone Caronni <negativo17@gmail.com> - 1.10.0-1.20220104gitaef6790
- Update to 1.10.0 plus latest commits.

* Thu Dec 02 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-3.20211202gitd6b2841
- Update to latest snapshot.

* Thu Sep 02 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-2
- Move unversioned library to main package.
- Drop devel subpackage.

* Tue Apr 13 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-1
- First build.

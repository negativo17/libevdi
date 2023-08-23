%global commit0 bdc258b25df4d00f222fde0e3c5003bf88ef17b5
%global date 20230223
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Name:       libevdi
Version:    1.14.1
Release:    1%{?dist}
Summary:    DisplayLink VGA/HDMI driver library
# See https://github.com/DisplayLink/evdi/blob/devel/README.md#licensing
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
%{_libdir}/libevdi.so.1
%{_libdir}/libevdi.so.%{version}

%changelog
* Wed Aug 23 2023 Simone Caronni <negativo17@gmail.com> - 1.14.1-1
- Update to 1.14.1.

* Fri Jun 02 2023 Simone Caronni <negativo17@gmail.com> - 1.14.0-1
- Update to 1.14.0.

* Wed Mar 29 2023 Simone Caronni <negativo17@gmail.com> - 1.13.1-1
- Update to 1.13.1.

* Fri Mar 17 2023 Simone Caronni <negativo17@gmail.com> - 1.13.0-1
- Update to 1.13.0.

* Thu Mar 02 2023 Simone Caronni <negativo17@gmail.com> - 1.12.0-3.20230223gitbdc258b
- Update to latest snapshot to align with kernel module packages (no change to
  the library).

* Thu Oct 13 2022 Simone Caronni <negativo17@gmail.com> - 1.12.0-2.20221013gitbdc258b
- Update to latest snapshot.

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

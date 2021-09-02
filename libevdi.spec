Name:       libevdi
Version:    1.9.1
Release:    2%{?dist}
Summary:    DisplayLink VGA/HDMI driver library
License:    LGPLv2+
URL:        https://github.com/DisplayLink/evdi

Source0:    https://github.com/DisplayLink/evdi/archive/v%{version}.tar.gz#/evdi-%{version}.tar.gz
Patch0:     https://github.com/DisplayLink/evdi/commit/0f1ad2153de1bc144f2359afa91fbe3fa07e9e7a.patch

BuildRequires:  gcc
BuildRequires:  libdrm-devel
BuildRequires:  make

%description
This adds support for HDMI/VGA adapters built upon the DisplayLink DL-6xxx,
DL-5xxx, DL-41xx and DL-3xxx series of chipsets. This includes numerous docking
stations, USB monitors, and USB adapters.

%prep
%autosetup -p1 -n evdi-%{version}

%build
cd library
%{set_build_flags}
%make_build

%install
install -D -m755 library/libevdi.so.%{version} %{buildroot}%{_libdir}/libevdi.so.%{version}
ldconfig -vn %{buildroot}%{_libdir}/
ln -sf libevdi.so.%{version} %{buildroot}%{_libdir}/libevdi.so

%files
%doc README.md
%license library/LICENSE
# DisplayLinkManager dlopens unversioned shared object:
%{_libdir}/libevdi.so
%{_libdir}/libevdi.so.0
%{_libdir}/libevdi.so.%{version}

%changelog
* Thu Sep 02 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-2
- Move unversioned library to main package.
- Drop devel subpackage.

* Tue Apr 13 2021 Simone Caronni <negativo17@gmail.com> - 1.9.1-1
- First build.

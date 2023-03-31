%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary: Manage MyKey devices
Name:    mikai
Version: 4.0.1
Release: 2
License: MIKAI LICENSE
URL:     https://telegram.me/mikaidownload
Source0: lib%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(libnfc)

%description
%{name} allows to manage MyKey devices, manufactured by a well known Italian company.

%package -n %{libname}
Summary:  %{summary}
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{name} runtime libraries.

%package -n %{devname}
Summary:  %{summary}
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{name} development headers and libraries.

%prep
%autosetup -n lib%{name}-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}*.so

%files -n %{devname}
%doc docs
%doc README.md
%license LICENSE
%{_includedir}/%{name}

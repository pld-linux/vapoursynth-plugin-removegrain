#
# Conditional build:
%bcond_with	sse2	# SSE2 instructions (no runtime detection)

%ifarch pentium4 %{x8664} x32
%define	with_sse2	1
%endif
Summary:	RemoveGrain plugin for Vapoursynth
Summary(pl.UTF-8):	Wtyczka RemoveGrain dla programu Vapoursynth
Name:		vapoursynth-plugin-removegrain
Version:	1
Release:	1
License:	WTFPL v2/MIT
Group:		Libraries
Source0:	https://github.com/vapoursynth/vs-removegrain/archive/R%{version}/vs-removegrain-R%{version}.tar.gz
# Source0-md5:	6a1c1954bedf512cff868c31311839b3
Patch0:		vs-removegrain-meson.patch
URL:		https://github.com/vapoursynth/vs-removegrain
BuildRequires:	libstdc++-devel
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vapoursynth port of RemoveGrain and Repair plugins from Avisynth.

%description -l pl.UTF-8
Port wtyczek Removegrain i Repair z programu Avisynth do programu
Vapoursynth.

%prep
%setup -q -n vs-removegrain-R%{version}
%patch -P0 -p1

%build
%if %{with sse2}
CPPFLAGS="%{rpmcppflags} -DVS_TARGET_CPU_X86"
CXXFLAGS="%{rpmcxxflags} -msse2 -mfpmath=sse"
%endif
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/rgvs.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libremovegrain.so

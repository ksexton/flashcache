%{?!kernel:%define kernel %(rpm -q kernel-devel | tail -1 | sed -e 's|kernel-devel-||')}
%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')
%define kernel_moduledir /lib/modules/%{kernel}
%define kernel_src_path %{kernel_moduledir}/source

Summary: A write-back block cache for Linux
Name: flashcache
Vendor: flashcache development, https://github.com/facebook/flashcache
Version: 1.0.20140121git
Release: 3%{?dist}
License: GPL
Group: System Environment/Base
URL: https://github.com/facebook/flashcache/
Packager: Hajime Taira <htaira@redhat.com>
Source0: %{name}-%{version}.tar.gz
Requires(post): /sbin/chkconfig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: x86_64
BuildRequires: tar gcc make kernel-devel rpm-build dkms yum-utils
ExclusiveArch: x86_64

%description
Flashcache : A write-back block cache for Linux

%package -n kmod-%{name}-%{kernel}
Summary: kernel modules for flashcache
Vendor: flashcache development, https://github.com/facebook/flashcache
Version: 1.0.20101201git
Release: 3%{?dist}
Group: System Environment/Kernel
Requires: kernel-uname-r = %{kernel}
Requires(post): /sbin/depmod
Requires(postun): /sbin/depmod

%description -n kmod-%{name}-%{kernel}
kernel modules for flashcache

%prep
%setup -q

%build
cd src/
make KERNEL_TREE=%{kernel_moduledir}/source/
# cd ../flashcache-wt/src/
# make KERNEL_TREE=%{kernel_moduledir}/source/

%install
install -o root -g root -m 0755 -d %{buildroot}/%{kernel_moduledir}/extra/flashcache
install -o root -g root -m 0755 src/flashcache.ko %{buildroot}/%{kernel_moduledir}/extra/flashcache/
# install -o root -g root -m 0755 flashcache-wt/src/flashcache-wt.ko %{buildroot}/%{kernel_moduledir}/extra/flashcache/
install -o root -g root -m 0755 -d %{buildroot}/sbin
install -o root -g root -m 0755 src/utils/flashcache_create %{buildroot}/sbin/
install -o root -g root -m 0755 src/utils/flashcache_destroy %{buildroot}/sbin/
install -o root -g root -m 0755 src/utils/flashcache_load %{buildroot}/sbin/
# install -o root -g root -m 0755 flashcache-wt/src/utils/flashcache_wt_create %{buildroot}/sbin/
# install -o root -g root -m 0755 -d %{buildroot}/%{_sysconfdir}/rc.d/init.d
# install -o root -g root -m 0755 -d %{buildroot}/%{_sysconfdir}/sysconfig
# install -o root -g root -m 0755 src/sysvinit/flashcache %{buildroot}/%{_sysconfdir}/rc.d/init.d/flashcache
# install -o root -g root -m 0644 src/sysconfig/flashcache %{buildroot}/%{_sysconfdir}/sysconfig/flashcache
install -o root -g root -m 0644 README %{buildroot}/sbin/
install -o root -g root -m 0755 -d %{buildroot}/usr/share/doc/%{name}-%{version}
install -o root -g root -m 0644 doc/flashcache-doc.txt %{buildroot}/usr/share/doc/%{name}-%{version}/
install -o root -g root -m 0644 doc/flashcache-sa-guide.txt %{buildroot}/usr/share/doc/%{name}-%{version}/

%clean
rm -rf %{buildroot}

%files
/sbin/*
/usr/share/doc/%{name}-%{version}/*
# %{_sysconfdir}/rc.d/init.d/flashcache
# %config(noreplace) %{_sysconfdir}/sysconfig/flashcache

%files -n kmod-%{name}-%{kernel}
%{kernel_moduledir}/extra/flashcache/*

%post
chkconfig --add flashcache

%post -n kmod-%{name}-%{kernel}
depmod -a %{kernel} >/dev/null 2>&1 || :

%postun -n kmod-%{name}-%{kernel}
depmod -a %{kernel} >/dev/null 2>&1 || :

%changelog
* Thu Feb 03 2011 13:00:00 +09:00 Hajime Taira <htaira@redhat.com>
- Split RPM package: flashcache and kmod-flashcache-<uname -r>

* Sun Dec 05 2010 13:00:00 +09:00 Hajime Taira <htaira@redhat.com>
- Initial build.

%changelog -n kmod-%{name}-%{kernel}
* Thu Feb 03 2011 13:00:00 +09:00 Hajime Taira <htaira@redhat.com>
- Split RPM package: flashcache and kmod-flashcache-<uname -r>

* Sun Dec 05 2010 13:00:00 +09:00 Hajime Taira <htaira@redhat.com>
- Initial build.

Name: nocache
Version: 0.9
Release: alt1

Summary: nocache - minimize filesystem caching effects
License: GPL
Group: <группа>

Url: https://github.com/Feh/nocache
Source: %name-%version.tar
Patch:
Packager: <ваше имя> <$login@altlinux.org>

PreReq:
Requires:
Provides:
Conflicts:

BuildPreReq:
BuildRequires:
BuildArch:

%description
The nocache tool tries to minimize the effect an application has on the Linux 
file system cache. This is done by intercepting the open and close system calls 
and calling posix_fadvise with the POSIX_FADV_DONTNEED parameter. Because the 
library remembers which pages (ie., 4K-blocks of the file) were already in file 
system cache when the file was opened, these will not be marked as "don't need",
because other applications might need that, although they are not actively used 
(think: hot standby).
Use case: backup processes that should not interfere with the present state of the cache.

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README

%changelog
* <дата> <ваше имя> <$login@altlinux.org> <версия-пакета>-<релиз пакета>
- initial build for ALT Linux Sisyphus
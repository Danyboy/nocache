Name: nocache
Version: 0.9
Release: alt1

Summary: nocache - minimize filesystem caching effects

License: GPL
Group: File tools
Url: https://github.com/Feh/nocache

Source: %name-%version.tar
Packager: Daniil Mikhailov <danil@etersoft.ru>

#PreReq:
#Requires:
#Provides:
#Conflicts:

#BuildPreReq:
#BuildRequires:
#BuildArch:

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
##%patch1 -p1

%build
#configure
# CFLAGS=-D_FILE_OFFSET_BITS=64
%make_build

%install
%makeinstall_std PREFIX=%prefix libdir=%buildroot/%_libdir

%check
#make_build check

%files
%_bindir/*
%_libdir/nocache.so
%_man1dir/*
%doc README COPYING

%changelog
* Mon Jul 08 2013 Daniil Mikhailov <danil@etersoft.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus

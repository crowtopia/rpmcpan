Name:           %{iov_prefix}-Capture-Tiny
Version:        0.24
Release:        1%{?dist}
Summary:        Capture STDOUT and STDERR from Perl, XS or external programs
License:        Apache Software License
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Capture-Tiny/
Source0:        http://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{iov_prefix}
Requires:       %{iov_prefix}

%description
Capture::Tiny provides a simple, portable way to capture almost anything
sent to STDOUT or STDERR, regardless of whether it comes from Perl, from XS
code or from an external program. Optionally, output can be teed so that it
is captured while being passed through to the original filehandles. Yes, it
even works on Windows (usually). Stop guessing which of a dozen capturing
modules to use in any particular situation and just use this one.

%prep
%setup -q -n Capture-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{vendormandir}/man3/*

%changelog
* Thu Jul 31 2014 David E. Wheeler <david.wheeler@iovation.com> 0.24-1
- Specfile autogenerated by cpanspec 1.78.

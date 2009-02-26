#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Natural
Summary:	DateTime::Format::Natural - Create machine readable date/time with natural parsing logic
#Summary(pl.UTF-8):	
Name:		perl-DateTime-Format-Natural
Version:	0.75_01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SC/SCHUBIGER/DateTime-Format-Natural-0.75_01.tar.gz
# Source0-md5:	d0ef45faab1ac80b3b00a2e57ef40f11
URL:		http://search.cpan.org/dist/DateTime-Format-Natural/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(boolean)
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-DateTime
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Params-Validate
BuildRequires:	perl(Test::MockTime)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime::Format::Natural takes a string with a human readable
date/time and creates a machine readable one by applying natural
parsing logic.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/DateTime/Format/*.pm
%{perl_vendorlib}/DateTime/Format/Natural
%{_mandir}/man?/*

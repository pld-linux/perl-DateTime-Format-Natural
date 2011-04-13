#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Natural
Summary:	DateTime::Format::Natural - Create machine readable date/time with natural parsing logic
Summary(pl.UTF-8):	DateTime::Format::Natural - Tworzy datę/czas dogodny dla maszyn
Name:		perl-DateTime-Format-Natural
Version:	0.94
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SC/SCHUBIGER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12a20eb7d5bb8f67199f6fa2126b581a
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

%description -l pl.UTF-8
DateTime::Format::Natural przyjmuje łańcuch znaków zawierający
datę/czas w formacie dogodnym dla ludzi i tworzy z niego format
dogodny dla maszyn.

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

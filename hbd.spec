Summary:	HomeBrew Java Decompiler
Summary(pl.UTF-8):   HomeBrew Java Decompiler - dekompilator Javy
Name:		hbd
Epoch:		0
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		Development/Languages/Java
Source0:	http://www.pdr.cx/dls/%{name}-%{version}.tar.gz
# Source0-md5:	fa0a3f07844d4d304be95d24fc91c30d
URL:		http://www.pdr.cx/projects/hbd/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Have you ever lost the source code to a Java program and thought there
was no way to get your code back? Well fret no longer, HomeBrew
Decompiler to the rescue! It's still far from perfect, but hopefully
it will be able to provide enough for you to reconstruct your lost
source file.

%description -l pl.UTF-8
Czy straciłeś kiedyś kod źródłowy programu w Javie i myślałeś, że nie
ma sposobu na odzyskanie go? Tak już nie jest, HomeBrew przyjdzie z
pomocą! Jeszcze mu daleko do perfekcji, ale miejmy nadzieję, że
umożliwi wystarczająco dużo, by odzyskać utracony plik źródłowy.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,NEWS,README,ChangeLog}
%attr(755,root,root) %{_bindir}/hbd
%{_mandir}/man1/hbd.1*

Summary:	A simple TODO manager
Name:		glista
Version:	0.4
Release:	5
License:	GPLv3
Group:		Office
Url:		http://prematureoptimization.org/glista/
Source0:	http://glista.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Glista aims to be a very simple personal to-do list manager 
that does what it's supposed to, and does not get in your way.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdv2011.0
+ Revision: 610862
- rebuild

* Sat Feb 13 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4-3mdv2010.1
+ Revision: 505578
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Nov 11 2008 Funda Wang <fwang@mandriva.org> 0.4-1mdv2009.1
+ Revision: 302044
- new version 0.4

* Fri Aug 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 277132
- import glista



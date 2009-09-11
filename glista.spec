Summary:	A simple TODO manager
Name:		glista
Version:	0.4
Release:	%mkrel 2
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

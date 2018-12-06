# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath         github.com/anmitsu/go-shlex
%global commit          648efa622239a2f6ff949fed78ee37b48d499ba4

%global common_description %{expand:
go-shlex is a library to make a lexical analyzer like Unix shell for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Library to make a lexical analyzer like Unix shell for golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git648efa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180421git648efa6
- First package for Fedora


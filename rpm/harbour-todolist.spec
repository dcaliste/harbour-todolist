# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-todolist

# >> macros
# << macros

Summary:    A simple todo list manager
Version:    1.0.2
Release:    1
Group:      Applications/Productivity
License:    GPLv3
URL:        https://github.com/ichthyosaurus/harbour-todolist
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-todolist.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
A simple todo list manager with support for multiple projects.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export VERSION_NUMBER=%{version}
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files

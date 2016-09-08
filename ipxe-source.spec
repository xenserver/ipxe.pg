%define src_name ipxe

Summary: iPXE source archive
Name: ipxe-source
Version: 1
Release: 1
License: GPLv2
Source0: http://hg.uk.xensource.com/git/carbon/%{branch}/ipxe.git/snapshot/refs/heads/master#/%{src_name}.tar.gz
BuildArch: noarch

%description
Ipxe specfile

%prep
%autosetup -p1

%build
mkdir -p ../%{src_name}
find . | cpio -pdmv ../%{src_name}

%install
mkdir -p %{buildroot}%{_usrsrc}
tar zcvf %{buildroot}%{_usrsrc}/%{name}.tar.gz -C .. %{src_name}

%files
%{_usrsrc}/%{name}.tar.gz

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : h5py
Version  : 2.6.0
Release  : 3
URL      : https://pypi.python.org/packages/22/82/64dada5382a60471f85f16eb7d01cc1a9620aea855cd665609adf6fdbb0d/h5py-2.6.0.tar.gz
Source0  : https://pypi.python.org/packages/22/82/64dada5382a60471f85f16eb7d01cc1a9620aea855cd665609adf6fdbb0d/h5py-2.6.0.tar.gz
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: h5py-python
BuildRequires : Cython-python
BuildRequires : hdf5-dev
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-pkgconfig
BuildRequires : setuptools
BuildRequires : six

%description
.. image:: https://travis-ci.org/h5py/h5py.png
:target: https://travis-ci.org/h5py/h5py

%package python
Summary: python components for the h5py package.
Group: Default

%description python
python components for the h5py package.


%prep
%setup -q -n h5py-2.6.0

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_autobuild
Version  : 2021.3.14
Release  : 13
URL      : https://files.pythonhosted.org/packages/df/a5/2ed1b81e398bc14533743be41bf0ceaa49d671675f131c4d9ce74897c9c1/sphinx-autobuild-2021.3.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/a5/2ed1b81e398bc14533743be41bf0ceaa49d671675f131c4d9ce74897c9c1/sphinx-autobuild-2021.3.14.tar.gz
Summary  : Rebuild Sphinx documentation on changes, with live-reload in the browser.
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_autobuild-bin = %{version}-%{release}
Requires: pypi-sphinx_autobuild-license = %{version}-%{release}
Requires: pypi-sphinx_autobuild-python = %{version}-%{release}
Requires: pypi-sphinx_autobuild-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
# sphinx-autobuild
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package bin
Summary: bin components for the pypi-sphinx_autobuild package.
Group: Binaries
Requires: pypi-sphinx_autobuild-license = %{version}-%{release}

%description bin
bin components for the pypi-sphinx_autobuild package.


%package license
Summary: license components for the pypi-sphinx_autobuild package.
Group: Default

%description license
license components for the pypi-sphinx_autobuild package.


%package python
Summary: python components for the pypi-sphinx_autobuild package.
Group: Default
Requires: pypi-sphinx_autobuild-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_autobuild package.


%package python3
Summary: python3 components for the pypi-sphinx_autobuild package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_autobuild)
Requires: pypi(colorama)
Requires: pypi(livereload)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinx_autobuild package.


%prep
%setup -q -n sphinx-autobuild-2021.3.14
cd %{_builddir}/sphinx-autobuild-2021.3.14
pushd ..
cp -a sphinx-autobuild-2021.3.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408712
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_autobuild
cp %{_builddir}/sphinx-autobuild-2021.3.14/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_autobuild/8093604dc0459c72dacab07a5a862b89708940d2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sphinx-autobuild

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_autobuild/8093604dc0459c72dacab07a5a862b89708940d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

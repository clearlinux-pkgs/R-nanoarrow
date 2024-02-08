#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: da8b975
#
Name     : R-nanoarrow
Version  : 0.4.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/nanoarrow_0.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nanoarrow_0.4.0.tar.gz
Summary  : Interface to the 'nanoarrow' 'C' Library
Group    : Development/Tools
License  : Apache-2.0
Requires: R-nanoarrow-lib = %{version}-%{release}
BuildRequires : R-blob
BuildRequires : R-hms
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
'Apache Arrow' application binary interface. Functions to import and
  export 'ArrowArray', 'ArrowSchema', and 'ArrowArrayStream' 'C' structures
  to and from 'R' objects are provided alongside helpers to facilitate zero-copy
  data transfer among 'R' bindings to libraries implementing the 'Arrow' 'C'
  data interface.

%package lib
Summary: lib components for the R-nanoarrow package.
Group: Libraries

%description lib
lib components for the R-nanoarrow package.


%prep
%setup -q -n nanoarrow
pushd ..
cp -a nanoarrow buildavx2
popd
pushd ..
cp -a nanoarrow buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707420052

%install
export SOURCE_DATE_EPOCH=1707420052
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nanoarrow/DESCRIPTION
/usr/lib64/R/library/nanoarrow/INDEX
/usr/lib64/R/library/nanoarrow/Meta/Rd.rds
/usr/lib64/R/library/nanoarrow/Meta/features.rds
/usr/lib64/R/library/nanoarrow/Meta/hsearch.rds
/usr/lib64/R/library/nanoarrow/Meta/links.rds
/usr/lib64/R/library/nanoarrow/Meta/nsInfo.rds
/usr/lib64/R/library/nanoarrow/Meta/package.rds
/usr/lib64/R/library/nanoarrow/NAMESPACE
/usr/lib64/R/library/nanoarrow/NEWS.md
/usr/lib64/R/library/nanoarrow/R/nanoarrow
/usr/lib64/R/library/nanoarrow/R/nanoarrow.rdb
/usr/lib64/R/library/nanoarrow/R/nanoarrow.rdx
/usr/lib64/R/library/nanoarrow/help/AnIndex
/usr/lib64/R/library/nanoarrow/help/aliases.rds
/usr/lib64/R/library/nanoarrow/help/nanoarrow.rdb
/usr/lib64/R/library/nanoarrow/help/nanoarrow.rdx
/usr/lib64/R/library/nanoarrow/help/paths.rds
/usr/lib64/R/library/nanoarrow/html/00Index.html
/usr/lib64/R/library/nanoarrow/html/R.css
/usr/lib64/R/library/nanoarrow/include/nanoarrow/r.h
/usr/lib64/R/library/nanoarrow/tests/testthat.R
/usr/lib64/R/library/nanoarrow/tests/testthat/_snaps/array-stream.md
/usr/lib64/R/library/nanoarrow/tests/testthat/_snaps/as-array.md
/usr/lib64/R/library/nanoarrow/tests/testthat/_snaps/buffer.md
/usr/lib64/R/library/nanoarrow/tests/testthat/test-altrep.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-array-stream.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-array.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-as-array.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-buffer.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-convert-array-stream.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-convert-array.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-extension-vctrs.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-extension.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-infer-ptype.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-nanoarrow-package.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-pkg-arrow.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-pointers.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-schema.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-type.R
/usr/lib64/R/library/nanoarrow/tests/testthat/test-util.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/nanoarrow/libs/nanoarrow.so
/usr/lib64/R/library/nanoarrow/libs/nanoarrow.so

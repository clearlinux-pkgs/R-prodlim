#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-prodlim
Version  : 2019.11.13
Release  : 43
URL      : https://cran.r-project.org/src/contrib/prodlim_2019.11.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/prodlim_2019.11.13.tar.gz
Summary  : Product-Limit Estimation for Censored Event History Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-prodlim-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-lava
BuildRequires : R-Rcpp
BuildRequires : R-lava
BuildRequires : buildreq-R

%description
for censored event history (survival) analysis. Kaplan-Meier and
    Aalen-Johansen method.

%package lib
Summary: lib components for the R-prodlim package.
Group: Libraries

%description lib
lib components for the R-prodlim package.


%prep
%setup -q -c -n prodlim
cd %{_builddir}/prodlim

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641079439

%install
export SOURCE_DATE_EPOCH=1641079439
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc prodlim || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/prodlim/DESCRIPTION
/usr/lib64/R/library/prodlim/INDEX
/usr/lib64/R/library/prodlim/Meta/Rd.rds
/usr/lib64/R/library/prodlim/Meta/features.rds
/usr/lib64/R/library/prodlim/Meta/hsearch.rds
/usr/lib64/R/library/prodlim/Meta/links.rds
/usr/lib64/R/library/prodlim/Meta/nsInfo.rds
/usr/lib64/R/library/prodlim/Meta/package.rds
/usr/lib64/R/library/prodlim/NAMESPACE
/usr/lib64/R/library/prodlim/R/prodlim
/usr/lib64/R/library/prodlim/R/prodlim.rdb
/usr/lib64/R/library/prodlim/R/prodlim.rdx
/usr/lib64/R/library/prodlim/help/AnIndex
/usr/lib64/R/library/prodlim/help/aliases.rds
/usr/lib64/R/library/prodlim/help/paths.rds
/usr/lib64/R/library/prodlim/help/prodlim.rdb
/usr/lib64/R/library/prodlim/help/prodlim.rdx
/usr/lib64/R/library/prodlim/html/00Index.html
/usr/lib64/R/library/prodlim/html/R.css
/usr/lib64/R/library/prodlim/tests/testthat/cluster.R
/usr/lib64/R/library/prodlim/tests/testthat/pseudo.R
/usr/lib64/R/library/prodlim/tests/testthat/test-prodlim.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/prodlim/libs/prodlim.so
/usr/lib64/R/library/prodlim/libs/prodlim.so.avx2
/usr/lib64/R/library/prodlim/libs/prodlim.so.avx512

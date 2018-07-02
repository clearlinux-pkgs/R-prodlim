#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-prodlim
Version  : 2018.04.18
Release  : 10
URL      : https://cran.r-project.org/src/contrib/prodlim_2018.04.18.tar.gz
Source0  : https://cran.r-project.org/src/contrib/prodlim_2018.04.18.tar.gz
Summary  : Product-Limit Estimation for Censored Event History Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-prodlim-lib
Requires: R-Rcpp
Requires: R-lava
BuildRequires : R-Rcpp
BuildRequires : R-lava
BuildRequires : clr-R-helpers

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524234691

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1524234691
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prodlim
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library prodlim|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/prodlim/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/prodlim/libs/prodlim.so
/usr/lib64/R/library/prodlim/libs/prodlim.so.avx2
/usr/lib64/R/library/prodlim/libs/prodlim.so.avx512

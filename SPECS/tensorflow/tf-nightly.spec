Summary:        TensorFlow is an open source machine learning framework for everyone.
Name:           tf-nightly
Version:        2.15.0
Release:        1%{?dist}
License:        ASL 2.0
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
Group:          Development/Languages/Python
URL:            https://www.tensorflow.org/
Source0:        https://github.com/tensorflow/tensorflow/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-cache2.tar.gz
BuildRequires:  bazel
BuildRequires:  binutils
BuildRequires:  build-essential
BuildRequires:  git
BuildRequires:  libstdc++-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-requests
BuildRequires:  python3-wheel
BuildRequires:  tar
BuildRequires:  which
ExclusiveArch:  x86_64

%description
TensorFlow is an open source machine learning framework for everyone.
tf-nightly is to break the dependency cycle : Tensorflow -> Keras, TensorBoard -> TensorFlow (tf-nightly)

%package -n python3-tf-nightly
Summary:        python-tensorflow
Requires:       python3-markupsafe
Requires:       python3-absl-py
Requires:       python3-astunparse
Requires:       python3-cachetools
Requires:       python3-charset-normalizer
Requires:       python3-devel
Requires:       python3-flatbuffers
Requires:       python3-gast
Requires:       python3-google-auth
Requires:       python3-google-pasta
Requires:       python3-google-auth-oauthlib
Requires:       python3-grpcio
Requires:       python3-h5py
Requires:       python3-idna
Requires:       python3-importlib-metadata
Requires:       python3-libclang
Requires:       python3-markdown
Requires:       python3-numpy
Requires:       python3-oauthlib
Requires:       python3-opt-einsum
Requires:       python3-protobuf
Requires:       python3-pyasn1
Requires:       python3-pyasn1-modules
Requires:       python3-requests-oauthlib
Requires:       python3-rsa
Requires:       python3-six
Requires:       python3-termcolor
Requires:       python3-typing-extensions
Requires:       python3-werkzeug
Requires:       python3-wrapt
Requires:       python3-zipp

%description -n python3-tf-nightly
TensorFlow is an open source machine learning framework for everyone.
tf-nightly is to break the dependency cycle : Tensorflow -> Keras, TensorBoard -> TensorFlow (tf-nightly)

%prep
%autosetup -p1


%build
MD5_HASH=$(echo -n $PWD | md5sum | awk '{print $1}')
mkdir -p /root/.cache/bazel/_bazel_$USER/$MD5_HASH/external
tar -xvf %{SOURCE1} -C /root/.cache/bazel/_bazel_$USER/$MD5_HASH/external

ln -s %{_bindir}/python3 %{_bindir}/python
# Remove the .bazelversion file so that latest bazel version available will be used to build TensorFlow.
rm .bazelversion

bazel --batch build  //tensorflow/tools/pip_package:build_pip_package


./bazel-bin/tensorflow/tools/pip_package/build_pip_package pyproject-wheeldir/




%install
python3 -m pip install --root /usr/src/azl/BUILDROOT/tensorflow-2.15.0-1.azl3.x86_64 --no-deps --disable-pip-version-check --progress-bar off --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links /usr/src/azl/BUILD/tensorflow-2.15.0/pyproject-wheeldir


%files -n python3-tf-nightly
%license LICENSE
%{python3_sitelib}/*


%changelog
* Tue Mar 05 2024 Riken Maharjan <rmaharjan@microsoft> - 2.15.0-1
- Update to 2.15.0

* Wed Oct 11 2023 Mitch Zhu <mitchzhu@microsoft> - 2.11.1-1
- Update to 2.11.1 to fix CVEs

* Tue Aug 01 2023 Riken Maharjan <rmaharjan@microsoft.com> - 2.11.0-4
- Remove .bazelversion file.

* Thu Jan 03 2022 Riken Maharjan <rmaharjan@microsoft> - 2.11.0-3
- Add tf-nightly subpackage. 

* Thu Dec 08 2022 Riken Maharjan <rmaharjan@microsoft> - 2.11.0-2
- Correct markupsafe package name. 

* Sun Dec 04 2022 Riken Maharjan <rmaharjan@microsoft> - 2.11.0-1
- Update to 2.11.0

* Thu Sep 22 2022 Riken Maharjan <rmaharjan@microsoft> - 2.8.3-1
- License verified
- Original version for CBL-Mariner
SPHINXBUILD   = ./.venv/bin/sphinx-build
SPHINXOPTS    =
SOURCEDIR     = docs
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
.PHONY: help
help: dependencies
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

./.venv/pyvenv.cfg:
	@echo "provisioning environment"
	@/usr/bin/env python3 -m venv ./.venv

.PHONY: dependencies
dependencies: ./.venv/pyvenv.cfg ./requirements.txt
	@echo "installing dependencies"
	@./.venv/bin/pip3 install -r ./requirements.txt

./requirements.txt:
	@

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
.PHONY: Makefile
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

import email.header

                if self.filename == '.gitmodules' or \
                   self.filename == 'BaseTools/Conf/diff.order':
                    # .gitmodules and diff orderfiles are used internally by git
                    # use tabs and LF line endings.  Do not enforce no tabs and
                    # do not enforce CR/LF line endings.
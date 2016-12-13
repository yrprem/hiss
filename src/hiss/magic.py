import os
import sys

from IPython.core.magic import magics_class, line_magic
import IPython.terminal.embed


@magics_class
class PatchedEmbeddedMagics(IPython.terminal.embed.EmbeddedMagics):
    @line_magic
    def pex(self, entry_point):
        if entry_point:
            sys.path[0] = os.path.abspath(sys.path[0])
            sys.path.insert(0, entry_point)
            sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))
            from _pex import pex_bootstrapper
            pex_bootstrapper.bootstrap_pex_env(entry_point)
            print("Bootstrapped into pex {0}.".format(entry_point))
        else:
            print("No pex provided! Doing nothing.")


setattr(IPython.terminal.embed, 'EmbeddedMagics', PatchedEmbeddedMagics)

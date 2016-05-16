###
# Copyright (c) 2013-2014, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Hardball')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Hardball', True)


Hardball = conf.registerPlugin('Hardball')
# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(Hardball, 'logURLs', registry.Boolean(False, """Should we log all URL calls?"""))
conf.registerGlobalValue(Hardball, 'checkInterval', registry.NonNegativeInteger(10, """Positive Integer in seconds to check."""))
conf.registerChannelValue(Hardball, 'prefix', registry.Boolean(False, """Should we prefix output with the string"""))
conf.registerChannelValue(Hardball, 'prefixString', registry.String("MLB: ", """Prefix String."""))
conf.registerChannelValue(Hardball, 'inningToAnnounceNoHitter', registry.NonNegativeInteger(7, """Inning to announce when no-hitters are being thrown."""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

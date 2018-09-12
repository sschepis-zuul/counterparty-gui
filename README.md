zuul-gui
================

# Description

`zuul-gui` is a PyQT5 GUI for [`zuul-lib`](https://github.com/ZuulZUL/zuuld).

# Requirements

* [Python 3](http://python.org)
* [PyQT5](http://www.riverbankcomputing.com/software/pyqt/download5)
* [`zuul-cli`](https://github.com/ZuulZUL/zuul-cli)
* [`Gozer Core`](https://gozer.org/en/download) OR [`gzrwallet`](https://github.com/gzrsuite/gzrwallet)

# Installation and usage

**With installer**

Download and execute Windows (or MacOS installer) [installer](https://github.com/ZuulZUL/zuul-gui/releases).

**From source**

```
$ git clone https://github.com/ZuulZUL/zuul-gui.git
$ cd zuul-gui
$ pip3 install -r requirements.txt
$ python3 setup.py install
$ ./zuul-gui.py --help
```

# Plugins

In zuul-gui everything is a plugin. The core application only manages the left menu. Each plugin adds one or more items in this menu. When the user clicks on one of these items, the core application displays the corresponding plugin in the main window.

A plugin is defined by the following conventions:

* it must live in the folder `plugins/{PLUGIN_NAME}/`
* PLUGIN_NAME folder must contains at least one file `index.qml` that contains the QML root object
* the root object in `index.qml` must contains 3 javascript callbacks: 
    
    - `init()`, called once, when the application initialises plugins.  
    - `onMenuAction(itemValue)`, called when the user clicks on a menu item that belongs to the plugin.
    - `onMessage(messageName, messageData)`, for now called only when a new block is parsed by the Zuul server with `messageName` equal to `new_block`.

* the root object in `index.qml` must contains a property `root.menu`. It contains the list of items to dsplay in the left menu and can be populated in the `init()` callback. 
* the QML context contains:
    - an instance of ZuuldAPI (core/api.py) to make any RPC call to the zuuld API or the Wallet with Javascript, 
    - an instance of GUI (core/gui.py) to display messages or ask confirmations.

Example:

```
	function sendAsset() {
		// prepare the query
        var query = {
            'method': 'create_send',
            'params': {
                'source':  sendFormComp.source,
                'destination': sendFormComp.destination,
                'asset': root.currentAsset,
                'quantity': sendFormComp.quantity
            }
        }

        // prepare the confirmation message
        var confirmMessage = "Do you really want to send " +
                             sendFormComp.quantity + " " + root.currentAsset +
                             " to " + sendFormComp.destination;

        if (GUI.confirm("Confirm send", confirmMessage)) {
            // Compose transaction
            var unsigned_hex = zulApi.call(query);
            if (unsigned_hex) {
                // Sign transaction
                var signed_hex = zulApi.call({'method': 'sign_raw_transaction', 'params': {'tx_hex': unsigned_hex}});
                if (signed_hex) {
                    // Broadcast transaction
                    var tx_hash = zulApi.call({'method': 'send_raw_transaction', 'params': {'tx_hex': signed_hex}});
                    // display transaction hash
                    if (tx_hash) {
                        GUI.alert("Transaction done", tx_hash);
                    }
                }
            }
        }
    }
```





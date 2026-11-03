# 3.4. Channel

A _channel_ defines a stream of updates for an Operator and is used to roll out updates for subscribers. The head points to the latest version of that channel. For example, a `stable` channel would have all stable versions of an Operator arranged from the earliest to the latest. 

An Operator can have several channels, and a subscription binding to a certain channel would only look for updates in that channel.

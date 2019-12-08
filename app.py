#!/usr/bin/env python3

from aws_cdk import core

from devops.devops_stack import DevopsStack


app = core.App()
DevopsStack(app, "devops")

app.synth()

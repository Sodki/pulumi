# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ResourceArgs', 'Resource']

@pulumi.input_type
class ResourceArgs:
    def __init__(__self__, *,
                 config: pulumi.Input['ConfigArgs'],
                 config_array: pulumi.Input[Sequence[pulumi.Input['ConfigArgs']]],
                 config_map: pulumi.Input[Mapping[str, pulumi.Input['ConfigArgs']]],
                 foo: pulumi.Input[str],
                 foo_array: pulumi.Input[Sequence[pulumi.Input[str]]],
                 foo_map: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        """
        The set of arguments for constructing a Resource resource.
        """
        ResourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            config=config,
            config_array=config_array,
            config_map=config_map,
            foo=foo,
            foo_array=foo_array,
            foo_map=foo_map,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             config: pulumi.Input['ConfigArgs'],
             config_array: pulumi.Input[Sequence[pulumi.Input['ConfigArgs']]],
             config_map: pulumi.Input[Mapping[str, pulumi.Input['ConfigArgs']]],
             foo: pulumi.Input[str],
             foo_array: pulumi.Input[Sequence[pulumi.Input[str]]],
             foo_map: pulumi.Input[Mapping[str, pulumi.Input[str]]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("config", config)
        _setter("config_array", config_array)
        _setter("config_map", config_map)
        _setter("foo", foo)
        _setter("foo_array", foo_array)
        _setter("foo_map", foo_map)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input['ConfigArgs']:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input['ConfigArgs']):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="configArray")
    def config_array(self) -> pulumi.Input[Sequence[pulumi.Input['ConfigArgs']]]:
        return pulumi.get(self, "config_array")

    @config_array.setter
    def config_array(self, value: pulumi.Input[Sequence[pulumi.Input['ConfigArgs']]]):
        pulumi.set(self, "config_array", value)

    @property
    @pulumi.getter(name="configMap")
    def config_map(self) -> pulumi.Input[Mapping[str, pulumi.Input['ConfigArgs']]]:
        return pulumi.get(self, "config_map")

    @config_map.setter
    def config_map(self, value: pulumi.Input[Mapping[str, pulumi.Input['ConfigArgs']]]):
        pulumi.set(self, "config_map", value)

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Input[str]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: pulumi.Input[str]):
        pulumi.set(self, "foo", value)

    @property
    @pulumi.getter(name="fooArray")
    def foo_array(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "foo_array")

    @foo_array.setter
    def foo_array(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "foo_array", value)

    @property
    @pulumi.getter(name="fooMap")
    def foo_map(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        return pulumi.get(self, "foo_map")

    @foo_map.setter
    def foo_map(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "foo_map", value)


class Resource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['ConfigArgs']]] = None,
                 config_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigArgs']]]]] = None,
                 config_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ConfigArgs']]]]] = None,
                 foo: Optional[pulumi.Input[str]] = None,
                 foo_array: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 foo_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Resource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Resource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResourceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[pulumi.InputType['ConfigArgs']]] = None,
                 config_array: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConfigArgs']]]]] = None,
                 config_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ConfigArgs']]]]] = None,
                 foo: Optional[pulumi.Input[str]] = None,
                 foo_array: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 foo_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceArgs.__new__(ResourceArgs)

            if not isinstance(config, ConfigArgs):
                config = config or {}
                def _setter(key, value):
                    config[key] = value
                ConfigArgs._configure(_setter, **config)
            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = None if config is None else pulumi.Output.secret(config)
            if config_array is None and not opts.urn:
                raise TypeError("Missing required property 'config_array'")
            __props__.__dict__["config_array"] = None if config_array is None else pulumi.Output.secret(config_array)
            if config_map is None and not opts.urn:
                raise TypeError("Missing required property 'config_map'")
            __props__.__dict__["config_map"] = None if config_map is None else pulumi.Output.secret(config_map)
            if foo is None and not opts.urn:
                raise TypeError("Missing required property 'foo'")
            __props__.__dict__["foo"] = None if foo is None else pulumi.Output.secret(foo)
            if foo_array is None and not opts.urn:
                raise TypeError("Missing required property 'foo_array'")
            __props__.__dict__["foo_array"] = None if foo_array is None else pulumi.Output.secret(foo_array)
            if foo_map is None and not opts.urn:
                raise TypeError("Missing required property 'foo_map'")
            __props__.__dict__["foo_map"] = None if foo_map is None else pulumi.Output.secret(foo_map)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["config", "configArray", "configMap", "foo", "fooArray", "fooMap"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Resource, __self__).__init__(
            'mypkg::Resource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Resource':
        """
        Get an existing Resource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceArgs.__new__(ResourceArgs)

        __props__.__dict__["config"] = None
        __props__.__dict__["config_array"] = None
        __props__.__dict__["config_map"] = None
        __props__.__dict__["foo"] = None
        __props__.__dict__["foo_array"] = None
        __props__.__dict__["foo_map"] = None
        return Resource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.Config']:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="configArray")
    def config_array(self) -> pulumi.Output[Sequence['outputs.Config']]:
        return pulumi.get(self, "config_array")

    @property
    @pulumi.getter(name="configMap")
    def config_map(self) -> pulumi.Output[Mapping[str, 'outputs.Config']]:
        return pulumi.get(self, "config_map")

    @property
    @pulumi.getter
    def foo(self) -> pulumi.Output[str]:
        return pulumi.get(self, "foo")

    @property
    @pulumi.getter(name="fooArray")
    def foo_array(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "foo_array")

    @property
    @pulumi.getter(name="fooMap")
    def foo_map(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "foo_map")


# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pleer_pb2 as pleer__pb2


class ProductsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ShowProducts = channel.unary_unary(
                '/Products/ShowProducts',
                request_serializer=pleer__pb2.ProductInfoRequest.SerializeToString,
                response_deserializer=pleer__pb2.ProductInfoResponse.FromString,
                )


class ProductsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ShowProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ShowProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.ShowProducts,
                    request_deserializer=pleer__pb2.ProductInfoRequest.FromString,
                    response_serializer=pleer__pb2.ProductInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Products', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Products(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ShowProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Products/ShowProducts',
            pleer__pb2.ProductInfoRequest.SerializeToString,
            pleer__pb2.ProductInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchProduct = channel.unary_unary(
                '/Search/SearchProduct',
                request_serializer=pleer__pb2.SearchRequest.SerializeToString,
                response_deserializer=pleer__pb2.SearchResponse.FromString,
                )


class SearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchProduct(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchProduct,
                    request_deserializer=pleer__pb2.SearchRequest.FromString,
                    response_serializer=pleer__pb2.SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Search', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Search(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Search/SearchProduct',
            pleer__pb2.SearchRequest.SerializeToString,
            pleer__pb2.SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

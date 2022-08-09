# Copyright 2019-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import absolute_import

from mock import patch, Mock


@patch('sagemaker_pytorch_serving_container.default_pytorch_inference_handler.DefaultPytorchInferenceHandler')
@patch('sagemaker_pytorch_serving_container.transformer.PyTorchTransformer')
def test_hosting_start(PyTorchTransformer, DefaultPytorchInferenceHandler):
    from sagemaker_pytorch_serving_container import handler_service

    handler_service.HandlerService()

    PyTorchTransformer.assert_called_with()


@patch('sagemaker_pytorch_serving_container.default_pytorch_inference_handler.DefaultPytorchInferenceHandler')
@patch('sagemaker_pytorch_serving_container.transformer.PyTorchTransformer')
def test_hosting_start_enable_multi_model(PyTorchTransformer, DefaultPytorchInferenceHandler):
    from sagemaker_pytorch_serving_container import handler_service

    context = Mock()
    context.system_properties.get.return_value = "/"
    handler_service.ENABLE_MULTI_MODEL = True
    handler = handler_service.HandlerService()
    handler.initialize(context)
    handler_service.ENABLE_MULTI_MODEL = False

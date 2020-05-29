# vidispine.WaveformApi

All URIs are relative to *http://localhost:8080/API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_waveform**](WaveformApi.md#get_item_waveform) | **GET** /item/{item-id}/waveform/values | Get waveform data
[**get_item_waveform_all_tracks**](WaveformApi.md#get_item_waveform_all_tracks) | **GET** /item/{item-id}/waveform/alltracks | Get waveform images for all audio channels
[**get_item_waveform_image**](WaveformApi.md#get_item_waveform_image) | **GET** /item/{item-id}/waveform/image | Get waveform image
[**get_item_waveform_image_uri**](WaveformApi.md#get_item_waveform_image_uri) | **GET** /item/{item-id}/waveform/imageURI | Get waveform image URI


# **get_item_waveform**
> WaveformDataType get_item_waveform(item_id, shape=shape, d_b=d_b, tag=tag, start=start, item_track=item_track, end=end, width=width, channel=channel, stream=stream)

Get waveform data

Returns the waveform data as a *WaveformDataDocument*.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.WaveformApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape = 'shape_example' # str | The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. (optional)
d_b = False # bool | - `true` - Return RMS dB values.  - `false` (default) - Return RMS 1-based absolute values. (optional) (default to False)
tag = 'original' # str | The shape tag to use. (optional) (default to 'original')
start = '-INF' # str | The start time code to get waveform information for. (optional) (default to '-INF')
item_track = 'item_track_example' # str | The `itemTrack` value of the audio channel within the shape. (optional)
end = '+INF' # str | The end time code to get waveform information for. (optional) (default to '+INF')
width = 400 # int | The number of sample points to return. (optional) (default to 400)
channel = '0' # str | The channel value of the audio channel within the stream of the component.  If `itemTrack` and `stream` are omitted, this value can be used to denote tracks in a linear fashion, regardless of `itemTrack` and `stream`.  Then `channel=0` means the first audio track, <pre>channel=1`</pre> the second, etc. (optional) (default to '0')
stream = 'stream_example' # str | The stream value of the audio channel within the component of the shape. (optional)

try:
    # Get waveform data
    api_response = api_instance.get_item_waveform(item_id, shape=shape, d_b=d_b, tag=tag, start=start, item_track=item_track, end=end, width=width, channel=channel, stream=stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaveformApi->get_item_waveform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape** | **str**| The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. | [optional] 
 **d_b** | **bool**| - &#x60;true&#x60; - Return RMS dB values.  - &#x60;false&#x60; (default) - Return RMS 1-based absolute values. | [optional] [default to False]
 **tag** | **str**| The shape tag to use. | [optional] [default to &#39;original&#39;]
 **start** | **str**| The start time code to get waveform information for. | [optional] [default to &#39;-INF&#39;]
 **item_track** | **str**| The &#x60;itemTrack&#x60; value of the audio channel within the shape. | [optional] 
 **end** | **str**| The end time code to get waveform information for. | [optional] [default to &#39;+INF&#39;]
 **width** | **int**| The number of sample points to return. | [optional] [default to 400]
 **channel** | **str**| The channel value of the audio channel within the stream of the component.  If &#x60;itemTrack&#x60; and &#x60;stream&#x60; are omitted, this value can be used to denote tracks in a linear fashion, regardless of &#x60;itemTrack&#x60; and &#x60;stream&#x60;.  Then &#x60;channel&#x3D;0&#x60; means the first audio track, &lt;pre&gt;channel&#x3D;1&#x60;&lt;/pre&gt; the second, etc. | [optional] [default to &#39;0&#39;]
 **stream** | **str**| The stream value of the audio channel within the component of the shape. | [optional] 

### Return type

[**WaveformDataType**](WaveformDataType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_waveform_all_tracks**
> str get_item_waveform_all_tracks(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)

Get waveform images for all audio channels

Solely used for debugging. May be deprecated in newer releases.  Returns a HTML document including image references to waveform images for all channels. Query parameters can be used to control the image appearance.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.WaveformApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape = 'shape_example' # str | The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. (optional)
tag = 'original' # str | The shape tag to use. (optional) (default to 'original')
height = 56 # int | The height, in pixels, of the image.  Default is 100. (optional)
vgridline = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
bgcolor = '#000000' # str | The background color of the image, as hex triplet. (optional) (default to '#000000')
end = '+INF' # str | The end time code to get waveform information for. (optional) (default to '+INF')
max = 3.4 # float | The audio value that corresponds the top border.  Defaults to `1` if `dB` is `false`, and `0` otherwise. (optional)
width = 400 # int | The number of sample points to return. (optional) (default to 400)
channel = '0' # str | The channel value of the audio channel within the stream of the component.  If `itemTrack` and `stream` are omitted, this value can be used to denote tracks in a linear fashion, regardless of `itemTrack` and `stream`.  Then `channel=0` means the first audio track, <pre>channel=1`</pre> the second, etc. (optional) (default to '0')
hgridline = '""' # str | The position of primary horizontal gridlines, in units of the audio. (optional) (default to '""')
vgridline2 = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
min = 3.4 # float | The audio value that corresponds the bottom border.  Defaults to `-1` if `dB` is `false`, and `-80` otherwise. (optional)
item_track = 'item_track_example' # str | The `itemTrack` value of the audio channel within the shape. (optional)
d_b = False # bool | - `true` - Return RMS dB values.  - `false` (default) - Return RMS 1-based absolute values. (optional) (default to False)
vgridlinecolor = '#808080' # str | The color of primary vertical gridlines (optional) (default to '#808080')
vgridline2color = '#404040' # str | The color of primary vertical gridlines (optional) (default to '#404040')
hgridline2 = '""' # str | The position of secondary horizontal gridlines, in units of the audio. (optional) (default to '""')
hgridlinecolor = '#808080' # str | The color of primary horizontal gridlines. (optional) (default to '#808080')
hgridline2color = '#404040' # str | The color of secondary horizontal gridlines (optional) (default to '#404040')
start = '-INF' # str | The start time code to get waveform information for. (optional) (default to '-INF')
fgcolor = '#ffffff' # str | The color of the waveform, as hex triplet. (optional) (default to '#ffffff')
stream = 'stream_example' # str | The stream value of the audio channel within the component of the shape. (optional)

try:
    # Get waveform images for all audio channels
    api_response = api_instance.get_item_waveform_all_tracks(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaveformApi->get_item_waveform_all_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape** | **str**| The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. | [optional] 
 **tag** | **str**| The shape tag to use. | [optional] [default to &#39;original&#39;]
 **height** | **int**| The height, in pixels, of the image.  Default is 100. | [optional] 
 **vgridline** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **bgcolor** | **str**| The background color of the image, as hex triplet. | [optional] [default to &#39;#000000&#39;]
 **end** | **str**| The end time code to get waveform information for. | [optional] [default to &#39;+INF&#39;]
 **max** | **float**| The audio value that corresponds the top border.  Defaults to &#x60;1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;0&#x60; otherwise. | [optional] 
 **width** | **int**| The number of sample points to return. | [optional] [default to 400]
 **channel** | **str**| The channel value of the audio channel within the stream of the component.  If &#x60;itemTrack&#x60; and &#x60;stream&#x60; are omitted, this value can be used to denote tracks in a linear fashion, regardless of &#x60;itemTrack&#x60; and &#x60;stream&#x60;.  Then &#x60;channel&#x3D;0&#x60; means the first audio track, &lt;pre&gt;channel&#x3D;1&#x60;&lt;/pre&gt; the second, etc. | [optional] [default to &#39;0&#39;]
 **hgridline** | **str**| The position of primary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **vgridline2** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **min** | **float**| The audio value that corresponds the bottom border.  Defaults to &#x60;-1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;-80&#x60; otherwise. | [optional] 
 **item_track** | **str**| The &#x60;itemTrack&#x60; value of the audio channel within the shape. | [optional] 
 **d_b** | **bool**| - &#x60;true&#x60; - Return RMS dB values.  - &#x60;false&#x60; (default) - Return RMS 1-based absolute values. | [optional] [default to False]
 **vgridlinecolor** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#808080&#39;]
 **vgridline2color** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#404040&#39;]
 **hgridline2** | **str**| The position of secondary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **hgridlinecolor** | **str**| The color of primary horizontal gridlines. | [optional] [default to &#39;#808080&#39;]
 **hgridline2color** | **str**| The color of secondary horizontal gridlines | [optional] [default to &#39;#404040&#39;]
 **start** | **str**| The start time code to get waveform information for. | [optional] [default to &#39;-INF&#39;]
 **fgcolor** | **str**| The color of the waveform, as hex triplet. | [optional] [default to &#39;#ffffff&#39;]
 **stream** | **str**| The stream value of the audio channel within the component of the shape. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A HTML document. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_waveform_image**
> file get_item_waveform_image(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)

Get waveform image

Returns an image with the waveform drawn on the canvas as described by the query parameters.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.WaveformApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape = 'shape_example' # str | The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. (optional)
tag = 'original' # str | The shape tag to use. (optional) (default to 'original')
height = 56 # int | The height, in pixels, of the image.  Default is 100. (optional)
vgridline = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
bgcolor = '#000000' # str | The background color of the image, as hex triplet. (optional) (default to '#000000')
end = '+INF' # str | The end time code to get waveform information for. (optional) (default to '+INF')
max = 3.4 # float | The audio value that corresponds the top border.  Defaults to `1` if `dB` is `false`, and `0` otherwise. (optional)
width = 400 # int | The number of sample points to return. (optional) (default to 400)
channel = '0' # str | The channel value of the audio channel within the stream of the component.  If `itemTrack` and `stream` are omitted, this value can be used to denote tracks in a linear fashion, regardless of `itemTrack` and `stream`.  Then `channel=0` means the first audio track, <pre>channel=1`</pre> the second, etc. (optional) (default to '0')
hgridline = '""' # str | The position of primary horizontal gridlines, in units of the audio. (optional) (default to '""')
vgridline2 = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
min = 3.4 # float | The audio value that corresponds the bottom border.  Defaults to `-1` if `dB` is `false`, and `-80` otherwise. (optional)
item_track = 'item_track_example' # str | The `itemTrack` value of the audio channel within the shape. (optional)
d_b = False # bool | - `true` - Return RMS dB values.  - `false` (default) - Return RMS 1-based absolute values. (optional) (default to False)
vgridlinecolor = '#808080' # str | The color of primary vertical gridlines (optional) (default to '#808080')
vgridline2color = '#404040' # str | The color of primary vertical gridlines (optional) (default to '#404040')
hgridline2 = '""' # str | The position of secondary horizontal gridlines, in units of the audio. (optional) (default to '""')
hgridlinecolor = '#808080' # str | The color of primary horizontal gridlines. (optional) (default to '#808080')
hgridline2color = '#404040' # str | The color of secondary horizontal gridlines (optional) (default to '#404040')
start = '-INF' # str | The start time code to get waveform information for. (optional) (default to '-INF')
fgcolor = '#ffffff' # str | The color of the waveform, as hex triplet. (optional) (default to '#ffffff')
stream = 'stream_example' # str | The stream value of the audio channel within the component of the shape. (optional)

try:
    # Get waveform image
    api_response = api_instance.get_item_waveform_image(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaveformApi->get_item_waveform_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape** | **str**| The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. | [optional] 
 **tag** | **str**| The shape tag to use. | [optional] [default to &#39;original&#39;]
 **height** | **int**| The height, in pixels, of the image.  Default is 100. | [optional] 
 **vgridline** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **bgcolor** | **str**| The background color of the image, as hex triplet. | [optional] [default to &#39;#000000&#39;]
 **end** | **str**| The end time code to get waveform information for. | [optional] [default to &#39;+INF&#39;]
 **max** | **float**| The audio value that corresponds the top border.  Defaults to &#x60;1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;0&#x60; otherwise. | [optional] 
 **width** | **int**| The number of sample points to return. | [optional] [default to 400]
 **channel** | **str**| The channel value of the audio channel within the stream of the component.  If &#x60;itemTrack&#x60; and &#x60;stream&#x60; are omitted, this value can be used to denote tracks in a linear fashion, regardless of &#x60;itemTrack&#x60; and &#x60;stream&#x60;.  Then &#x60;channel&#x3D;0&#x60; means the first audio track, &lt;pre&gt;channel&#x3D;1&#x60;&lt;/pre&gt; the second, etc. | [optional] [default to &#39;0&#39;]
 **hgridline** | **str**| The position of primary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **vgridline2** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **min** | **float**| The audio value that corresponds the bottom border.  Defaults to &#x60;-1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;-80&#x60; otherwise. | [optional] 
 **item_track** | **str**| The &#x60;itemTrack&#x60; value of the audio channel within the shape. | [optional] 
 **d_b** | **bool**| - &#x60;true&#x60; - Return RMS dB values.  - &#x60;false&#x60; (default) - Return RMS 1-based absolute values. | [optional] [default to False]
 **vgridlinecolor** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#808080&#39;]
 **vgridline2color** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#404040&#39;]
 **hgridline2** | **str**| The position of secondary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **hgridlinecolor** | **str**| The color of primary horizontal gridlines. | [optional] [default to &#39;#808080&#39;]
 **hgridline2color** | **str**| The color of secondary horizontal gridlines | [optional] [default to &#39;#404040&#39;]
 **start** | **str**| The start time code to get waveform information for. | [optional] [default to &#39;-INF&#39;]
 **fgcolor** | **str**| The color of the waveform, as hex triplet. | [optional] [default to &#39;#ffffff&#39;]
 **stream** | **str**| The stream value of the audio channel within the component of the shape. | [optional] 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | A PNG image. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_waveform_image_uri**
> str get_item_waveform_image_uri(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)

Get waveform image URI

Returns a URI that does not require authentication to the generated image. The URI expires after 1 hour.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vidispine
from vidispine.rest import ApiException
from pprint import pprint
configuration = vidispine.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = vidispine.WaveformApi(vidispine.ApiClient(configuration))
item_id = 'item_id_example' # str | The item id.
shape = 'shape_example' # str | The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. (optional)
tag = 'original' # str | The shape tag to use. (optional) (default to 'original')
height = 56 # int | The height, in pixels, of the image.  Default is 100. (optional)
vgridline = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
bgcolor = '#000000' # str | The background color of the image, as hex triplet. (optional) (default to '#000000')
end = '+INF' # str | The end time code to get waveform information for. (optional) (default to '+INF')
max = 3.4 # float | The audio value that corresponds the top border.  Defaults to `1` if `dB` is `false`, and `0` otherwise. (optional)
width = 400 # int | The number of sample points to return. (optional) (default to 400)
channel = '0' # str | The channel value of the audio channel within the stream of the component.  If `itemTrack` and `stream` are omitted, this value can be used to denote tracks in a linear fashion, regardless of `itemTrack` and `stream`.  Then `channel=0` means the first audio track, <pre>channel=1`</pre> the second, etc. (optional) (default to '0')
hgridline = '""' # str | The position of primary horizontal gridlines, in units of the audio. (optional) (default to '""')
vgridline2 = '""' # str | The position of primary vertical gridlines, where 0 is left border and 1 is right border. (optional) (default to '""')
min = 3.4 # float | The audio value that corresponds the bottom border.  Defaults to `-1` if `dB` is `false`, and `-80` otherwise. (optional)
item_track = 'item_track_example' # str | The `itemTrack` value of the audio channel within the shape. (optional)
d_b = False # bool | - `true` - Return RMS dB values.  - `false` (default) - Return RMS 1-based absolute values. (optional) (default to False)
vgridlinecolor = '#808080' # str | The color of primary vertical gridlines (optional) (default to '#808080')
vgridline2color = '#404040' # str | The color of primary vertical gridlines (optional) (default to '#404040')
hgridline2 = '""' # str | The position of secondary horizontal gridlines, in units of the audio. (optional) (default to '""')
hgridlinecolor = '#808080' # str | The color of primary horizontal gridlines. (optional) (default to '#808080')
hgridline2color = '#404040' # str | The color of secondary horizontal gridlines (optional) (default to '#404040')
start = '-INF' # str | The start time code to get waveform information for. (optional) (default to '-INF')
fgcolor = '#ffffff' # str | The color of the waveform, as hex triplet. (optional) (default to '#ffffff')
stream = 'stream_example' # str | The stream value of the audio channel within the component of the shape. (optional)

try:
    # Get waveform image URI
    api_response = api_instance.get_item_waveform_image_uri(item_id, shape=shape, tag=tag, height=height, vgridline=vgridline, bgcolor=bgcolor, end=end, max=max, width=width, channel=channel, hgridline=hgridline, vgridline2=vgridline2, min=min, item_track=item_track, d_b=d_b, vgridlinecolor=vgridlinecolor, vgridline2color=vgridline2color, hgridline2=hgridline2, hgridlinecolor=hgridlinecolor, hgridline2color=hgridline2color, start=start, fgcolor=fgcolor, stream=stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WaveformApi->get_item_waveform_image_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| The item id. | 
 **shape** | **str**| The shape id to use to get information from.  If omitted the shape tag will be used.  Note that an analysis of this shape must be done before the information is available. | [optional] 
 **tag** | **str**| The shape tag to use. | [optional] [default to &#39;original&#39;]
 **height** | **int**| The height, in pixels, of the image.  Default is 100. | [optional] 
 **vgridline** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **bgcolor** | **str**| The background color of the image, as hex triplet. | [optional] [default to &#39;#000000&#39;]
 **end** | **str**| The end time code to get waveform information for. | [optional] [default to &#39;+INF&#39;]
 **max** | **float**| The audio value that corresponds the top border.  Defaults to &#x60;1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;0&#x60; otherwise. | [optional] 
 **width** | **int**| The number of sample points to return. | [optional] [default to 400]
 **channel** | **str**| The channel value of the audio channel within the stream of the component.  If &#x60;itemTrack&#x60; and &#x60;stream&#x60; are omitted, this value can be used to denote tracks in a linear fashion, regardless of &#x60;itemTrack&#x60; and &#x60;stream&#x60;.  Then &#x60;channel&#x3D;0&#x60; means the first audio track, &lt;pre&gt;channel&#x3D;1&#x60;&lt;/pre&gt; the second, etc. | [optional] [default to &#39;0&#39;]
 **hgridline** | **str**| The position of primary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **vgridline2** | **str**| The position of primary vertical gridlines, where 0 is left border and 1 is right border. | [optional] [default to &#39;&quot;&quot;&#39;]
 **min** | **float**| The audio value that corresponds the bottom border.  Defaults to &#x60;-1&#x60; if &#x60;dB&#x60; is &#x60;false&#x60;, and &#x60;-80&#x60; otherwise. | [optional] 
 **item_track** | **str**| The &#x60;itemTrack&#x60; value of the audio channel within the shape. | [optional] 
 **d_b** | **bool**| - &#x60;true&#x60; - Return RMS dB values.  - &#x60;false&#x60; (default) - Return RMS 1-based absolute values. | [optional] [default to False]
 **vgridlinecolor** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#808080&#39;]
 **vgridline2color** | **str**| The color of primary vertical gridlines | [optional] [default to &#39;#404040&#39;]
 **hgridline2** | **str**| The position of secondary horizontal gridlines, in units of the audio. | [optional] [default to &#39;&quot;&quot;&#39;]
 **hgridlinecolor** | **str**| The color of primary horizontal gridlines. | [optional] [default to &#39;#808080&#39;]
 **hgridline2color** | **str**| The color of secondary horizontal gridlines | [optional] [default to &#39;#404040&#39;]
 **start** | **str**| The start time code to get waveform information for. | [optional] [default to &#39;-INF&#39;]
 **fgcolor** | **str**| The color of the waveform, as hex triplet. | [optional] [default to &#39;#ffffff&#39;]
 **stream** | **str**| The stream value of the audio channel within the component of the shape. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The URI to the image. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/recording.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18protobuf/recording.proto\x12\x08videoimu\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x06\n\nCameraInfo\x12\x18\n\x10intrinsic_params\x18\x01 \x03(\x02\x12\x19\n\x11\x64istortion_params\x18\x02 \x03(\x02\x12#\n\x1boptical_image_stabilization\x18\x03 \x01(\x08\x12\x1b\n\x13video_stabilization\x18\x04 \x01(\x08\x12\x1d\n\x15\x64istortion_correction\x18\n \x01(\x08\x12\x1a\n\x12sensor_orientation\x18\x0e \x01(\x05\x12@\n\x11\x66ocus_calibration\x18\x05 \x01(\x0e\x32%.videoimu.CameraInfo.FocusCalibration\x12>\n\x10timestamp_source\x18\x06 \x01(\x0e\x32$.videoimu.CameraInfo.TimestampSource\x12\x43\n\x13lens_pose_reference\x18\x07 \x01(\x0e\x32&.videoimu.CameraInfo.LensPoseReference\x12\x1a\n\x12lens_pose_rotation\x18\x08 \x03(\x02\x12\x1d\n\x15lens_pose_translation\x18\t \x03(\x02\x12-\n\nresolution\x18\x0b \x01(\x0b\x32\x19.videoimu.CameraInfo.Size\x12\x43\n pre_correction_active_array_size\x18\x0c \x01(\x0b\x32\x19.videoimu.CameraInfo.Size\x12!\n\x19original_intrinsic_params\x18\r \x03(\x02\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\"E\n\x10\x46ocusCalibration\x12\x10\n\x0cUNCALIBRATED\x10\x00\x12\x0f\n\x0b\x41PPROXIMATE\x10\x01\x12\x0e\n\nCALIBRATED\x10\x02\",\n\x0fTimestampSource\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08REALTIME\x10\x01\"E\n\x11LensPoseReference\x12\x12\n\x0ePRIMARY_CAMERA\x10\x00\x12\r\n\tGYROSCOPE\x10\x01\x12\r\n\tUNDEFINED\x10\x02\";\n\x15VideoFrameToTimestamp\x12\x0f\n\x07time_us\x18\x01 \x01(\x03\x12\x11\n\tframe_nbr\x18\x02 \x01(\x03\"\x82\x03\n\x12VideoFrameMetaData\x12\x0f\n\x07time_ns\x18\x01 \x01(\x03\x12\x14\n\x0c\x66rame_number\x18\x02 \x01(\x03\x12\x18\n\x10\x65xposure_time_ns\x18\x03 \x01(\x03\x12\x19\n\x11\x66rame_duration_ns\x18\x04 \x01(\x03\x12\x18\n\x10\x66rame_readout_ns\x18\x05 \x01(\x03\x12\x0b\n\x03iso\x18\x06 \x01(\x05\x12\x17\n\x0f\x66ocal_length_mm\x18\x07 \x01(\x02\x12\x1c\n\x14\x65st_focal_length_pix\x18\x08 \x01(\x02\x12\x1f\n\x17\x66ocus_distance_diopters\x18\t \x01(\x02\x12;\n\x0bOIS_samples\x18\n \x03(\x0b\x32&.videoimu.VideoFrameMetaData.OISSample\x12\x14\n\x0c\x66ocus_locked\x18\x0b \x01(\x08\x1a>\n\tOISSample\x12\x0f\n\x07time_ns\x18\x01 \x01(\x03\x12\x0f\n\x07x_shift\x18\x02 \x01(\x02\x12\x0f\n\x07y_shift\x18\x03 \x01(\x02\"\x90\x01\n\x07IMUInfo\x12\x11\n\tgyro_info\x18\x01 \x01(\t\x12\x17\n\x0fgyro_resolution\x18\x02 \x01(\x02\x12\x12\n\naccel_info\x18\x03 \x01(\t\x12\x18\n\x10\x61\x63\x63\x65l_resolution\x18\x04 \x01(\x02\x12\x18\n\x10sample_frequency\x18\x05 \x01(\x02\x12\x11\n\tplacement\x18\x06 \x03(\x02\"\x81\x02\n\x07IMUData\x12\x0f\n\x07time_ns\x18\x01 \x01(\x03\x12\x0c\n\x04gyro\x18\x02 \x03(\x02\x12\x12\n\ngyro_drift\x18\x03 \x03(\x02\x12\r\n\x05\x61\x63\x63\x65l\x18\x04 \x03(\x02\x12\x12\n\naccel_bias\x18\x05 \x03(\x02\x12\x31\n\rgyro_accuracy\x18\x06 \x01(\x0e\x32\x1a.videoimu.IMUData.Accuracy\x12\x32\n\x0e\x61\x63\x63\x65l_accuracy\x18\x07 \x01(\x0e\x32\x1a.videoimu.IMUData.Accuracy\"9\n\x08\x41\x63\x63uracy\x12\x0e\n\nUNRELIABLE\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03\"\xde\x01\n\x10VideoCaptureData\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x0b\x63\x61mera_meta\x18\x02 \x01(\x0b\x32\x14.videoimu.CameraInfo\x12#\n\x08imu_meta\x18\x03 \x01(\x0b\x32\x11.videoimu.IMUInfo\x12\x1e\n\x03imu\x18\x04 \x03(\x0b\x32\x11.videoimu.IMUData\x12\x30\n\nvideo_meta\x18\x05 \x03(\x0b\x32\x1c.videoimu.VideoFrameMetaData\"\xfd\x01\n\x0eMessageWrapper\x12+\n\x0b\x63\x61mera_meta\x18\x01 \x01(\x0b\x32\x14.videoimu.CameraInfoH\x00\x12%\n\x08imu_data\x18\x02 \x01(\x0b\x32\x11.videoimu.IMUDataH\x00\x12%\n\x08imu_meta\x18\x03 \x01(\x0b\x32\x11.videoimu.IMUInfoH\x00\x12\x32\n\nframe_meta\x18\x04 \x01(\x0b\x32\x1c.videoimu.VideoFrameMetaDataH\x00\x12\x35\n\nframe_time\x18\x05 \x01(\x0b\x32\x1f.videoimu.VideoFrameToTimestampH\x00\x42\x05\n\x03msgB.\n\x1bse.lth.math.videoimucaptureB\x0fRecordingProtosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.recording_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033se.lth.math.videoimucaptureB\017RecordingProtos'
  _CAMERAINFO._serialized_start=72
  _CAMERAINFO._serialized_end=898
  _CAMERAINFO_SIZE._serialized_start=673
  _CAMERAINFO_SIZE._serialized_end=710
  _CAMERAINFO_FOCUSCALIBRATION._serialized_start=712
  _CAMERAINFO_FOCUSCALIBRATION._serialized_end=781
  _CAMERAINFO_TIMESTAMPSOURCE._serialized_start=783
  _CAMERAINFO_TIMESTAMPSOURCE._serialized_end=827
  _CAMERAINFO_LENSPOSEREFERENCE._serialized_start=829
  _CAMERAINFO_LENSPOSEREFERENCE._serialized_end=898
  _VIDEOFRAMETOTIMESTAMP._serialized_start=900
  _VIDEOFRAMETOTIMESTAMP._serialized_end=959
  _VIDEOFRAMEMETADATA._serialized_start=962
  _VIDEOFRAMEMETADATA._serialized_end=1348
  _VIDEOFRAMEMETADATA_OISSAMPLE._serialized_start=1286
  _VIDEOFRAMEMETADATA_OISSAMPLE._serialized_end=1348
  _IMUINFO._serialized_start=1351
  _IMUINFO._serialized_end=1495
  _IMUDATA._serialized_start=1498
  _IMUDATA._serialized_end=1755
  _IMUDATA_ACCURACY._serialized_start=1698
  _IMUDATA_ACCURACY._serialized_end=1755
  _VIDEOCAPTUREDATA._serialized_start=1758
  _VIDEOCAPTUREDATA._serialized_end=1980
  _MESSAGEWRAPPER._serialized_start=1983
  _MESSAGEWRAPPER._serialized_end=2236
# @@protoc_insertion_point(module_scope)

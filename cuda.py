import pycuda.driver as cuda

# Initialize CUDA
cuda.init()

# Get the number of available GPUs (assuming one GPU for simplicity)
num_devices = cuda.Device.count()

if num_devices == 0:
    print("No CUDA devices found.")
else:
    # Choose the first GPU (change the device number if needed)
    device = cuda.Device(0)
    device_name = device.name()

    print(f"Using GPU: {device_name}")

    # Create a CUDA context (you can have multiple contexts on one GPU)
    ctx = device.make_context()

    try:
        # Allocate GPU memory
        size = 1024  # Size in bytes (adjust as needed)
        device_data = cuda.mem_alloc(size)

        # ... Use the GPU memory ...

        # Release GPU memory
        device_data.free()

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Reset the CUDA context to its initial state
        ctx.pop()

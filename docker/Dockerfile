FROM osgeo/gdal:ubuntu-small-3.6.3

# Create workspace directory
RUN mkdir -p /workspace

# Set working directory
WORKDIR /workspace

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install pandas
RUN pip install pandas

# Copy local script into the container
COPY create_shape.py /workspace/create_shape.py
COPY create_shape.py /workspace/read_shape.py

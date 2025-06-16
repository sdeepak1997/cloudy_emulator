from astropy.table import Table
# to read a fits file containing cloudy models
fits_file_path = "z_0_model.fits"
model_table = Table.read(fits_file_path)

# Display basic information about the table
print(f"Number of rows: {len(model_table)}")
print("\nColumn names:", model_table.colnames)

# Show a few rows of the table
print("\nFirst 5 rows of the table:")
print(model_table[:5])

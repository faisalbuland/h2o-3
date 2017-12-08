from __future__ import print_function
from builtins import str
from builtins import range
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.transforms.decomposition import H2OPCA


def pca_arrests():
  print("Importing USArrests.csv data...")
  arrestsH2O = h2o.upload_file(pyunit_utils.locate("smalldata/pca_test/USArrests.csv"))

  print("Testing to see whether the trained PCA are essentially the same using different implementation...")
  for impl in ["MTJ_EVD_DENSEMATRIX", "MTJ_EVD_SYMMMATRIX", "MTJ_SVD_DENSEMATRIX", "JAMA"]:
    model = H2OPCA(k = 4, pca_implementation=impl, seed=1234)
    model.train(x=list(range(4)), training_frame=arrestsH2O)

if __name__ == "__main__":
  pyunit_utils.standalone_test(pca_arrests)
else:
  pca_arrests()
